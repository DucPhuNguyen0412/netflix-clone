from core.models import Movie, Profile
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm

# Create your views here.
class Home(View):
    def get(self, request, *args, **kargs):
        if request.user.is_authenticated:
            return redirect('core:profile_list')
        return render(request,'index.html')
    
@method_decorator(login_required, name='dispatch')    
class ProfileList(View):
    def get(self, request, *args, **kargs):
        profile = request.user.profiles.all()

        return render(request, 'profileList.html', { 
                      'profiles':profile
        })
    
@method_decorator(login_required, name='dispatch') 
class ProfileCreate(View):
    def get(self, request, *args, **kargs):
        #form for creating profiles
        form = ProfileForm
        return render(request, 'profileCreate.html', {
            'form':form
        })
        
    def post(self, request, *args, **kargs):
        form=ProfileForm(request.POST or None)
        
        if form.is_valid():
            #form for creating profiles
           # print(form.cleaned_data)
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('core:profile_list')
            
        return render(request, 'profileCreate.html', {
            'form':form
        })

@method_decorator(login_required, name='dispatch') 
class Watch(View):
    def get(self, request, profile_id, *args, **kargs):
        try:
            profile=Profile.objects.get(uuid=profile_id)
            movies=Movie.objects.filter(age_limit=profile.age_limit)
            
            if profile not in request.user.profiles.all():
                return redirect(to='core:profile_list')
            
            return render(request, 'movieList.html', {
                'movies':movies
            })
        except Profile.DoesNotExist:
            return redirect(to='core:profile_list')
            