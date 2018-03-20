
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
import os


class Comment(models.Model):
	text = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')


class CardsSet(models.Model):
	name = models.CharField(max_length=255)
	educational_material = models.CharField(max_length = 10000)
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ManyToManyField(User)
	comments = GenericRelation(Comment)

	class Meta:
		indexes = [
    		models.Index(fields=['name','created_at',]),
		]
   

class Card(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    cardsSet = models. ManyToManyField(CardsSet)
    comments = GenericRelation(Comment)



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

class Friend(object):
	fromUser = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="Friend.fromUser+")
	toUser = models.ForeignKey(User,on_delete=models.SET_NULL, related_name="Friend.toUser+")
		


  


