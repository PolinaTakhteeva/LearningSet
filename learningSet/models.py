
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
import os


class Comment(models.Model):
	text = models.TextField()
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL);
	created_at = models.DateTimeField(auto_now_add=True)
	content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')


class CardsSet(models.Model): #group with rights
	name = models.CharField(max_length=255, db_index=True) #unic control  by data base
	educational_material = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, db_index=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE);
	comments = GenericRelation(Comment)
   

class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cardsSet = models. ManyToManyField(CardsSet)
    comments = GenericRelation(Comment)

	#delete user profile

# Many to many tables 

class Favorite(models.Model): #fk
	user = models.ForeignKey(User, on_delete=models.CASCADE);
	CardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE)

class TestGroup(models.Model):
	parentCardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE, related_name='TestGroup.parentCardsSet+')
	childCardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE, related_name='TestGroup.childCardsSet+')

# class Friend(object):#through
#  	fromUser = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="Friend.fromUser+")
# 	toUser = models.ForeignKey(User,on_delete=models.SET_NULL, related_name="Friend.toUser+")

def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)
		


  


