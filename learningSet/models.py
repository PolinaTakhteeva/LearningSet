
from django.db import models
from django.contrib.auth.models import User
import os

class CardsSet(models.Model):
	name = models.CharField(max_length=255)
	educational_material = models.CharField(max_length = 10000)
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ManyToManyField(User)

	class Meta:
		indexes = [
    		models.Index(fields=['name','created_at',]),
		]
   

class Card(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    cardsSet = models. ManyToManyField(CardsSet)


class Comment(models.Model):
	text = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)


def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)
		
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	specialty = models.CharField(max_length=255)

# Many to many tables 

class Favorite(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE);
	CardsSet = models.OneToOneField(CardsSet, on_delete=models.CASCADE)

class TestGroup(models.Model):
	parentCardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE, related_name='TestGroup.parentCardsSet+')
	childCardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE, related_name='TestGroup.childCardsSet+')


  


