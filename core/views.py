from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
    
class ProfileCreate(View):
    def get(self, request, *args, **kargs):
        #form for creating profiles
        return render(request, 'profileCreate.html')