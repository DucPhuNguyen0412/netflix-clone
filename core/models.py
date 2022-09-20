from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid #universal unique id

AGE_CHOICES=(
    ('All', 'All'), #first one is saved to the database, the second one is for the user
    ('Kids', 'Kids')
)

MOVIE_TYPE=(
    ('single', 'Single'),
    ('seasonal', 'Seasonal')
)

# Create your models here.
class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')
    
class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4) #create a random uuid
    
class Movie(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True) #add the time the movie created in the store
    uuid=models.UUIDField(default=uuid.uuid4)
    genre=models.CharField(max_length=10, choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    poster=models.ImageField(upload_to='poster', blank=True, null=True)
    age_limit=models.CharField(max_length=10, choices=AGE_CHOICES, null=True)
    
class Video(models.Model):
    title=models.CharField(max_length=225, blank=True, null=True)
    file=models.FileField(upload_to='movies')