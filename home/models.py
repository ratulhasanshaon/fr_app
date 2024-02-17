from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    face_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length = 100)
    job = models.CharField(max_length = 40)
    phone = models.CharField(max_length =  13)
    email = models.CharField(max_length = 25)
    bio = models.CharField(max_length = 200)
    image=models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name
    
    