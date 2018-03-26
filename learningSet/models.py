
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

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'


class CardsSet(models.Model): #group with rights
	name = models.CharField(max_length=255, db_index=True) #unic control  by data base
	description = models.TextField(null=True)
	educational_material = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True, db_index=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	comments = GenericRelation(Comment)

	class Meta:
		ordering = ('created_at',)
		verbose_name = 'Набор тестовых карт'
		verbose_name_plural = 'Наборы тестовых карт'
   

class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cardsSet = models. ManyToManyField(CardsSet)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = 'Флеш-карта'
        verbose_name_plural = 'Флеш-карты'

# Many to many tables 

class Favorite(models.Model): #fk
	user = models.ForeignKey(User, on_delete=models.CASCADE);
	CardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE)
	
	class Meta:
		verbose_name = 'Избранное'
		verbose_name_plural = 'Избранное'

class TestGroup(models.Model):
	parentCardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE, related_name='TestGroup.parentCardsSet+')
	childCardsSet = models.ForeignKey(CardsSet, on_delete=models.CASCADE, related_name='TestGroup.childCardsSet+')

		


  


