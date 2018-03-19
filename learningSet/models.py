
from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Card(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    # class Meta:
    #     verbose_name = 'Флеш-карта'
    #     verbose_name_plural = 'Флеш-карта'

class CardsSet(models.Model):
	name = models.CharField(max_length=255)
	educational_material = models.CharField(max_length = 10000)
	created_at = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #    verbose_name = 'Набор флеш-карт'
    #    verbose_name_plural = 'Наборы флеш-карт'

class Comment(models.Model):
	text = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)



def get_image_path(instance, filename):
		return os.path.join('photos', str(instance.id), filename)
		
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	specialty = models.CharField(max_length=255)


  


