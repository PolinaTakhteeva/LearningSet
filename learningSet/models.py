
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation


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
	name = models.CharField(max_length=255, db_index=True)
	description = models.TextField(null=True)
	educational_material = models.TextField(null=True)
	created_at = models.DateTimeField(auto_now_add=True, db_index=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	comments = GenericRelation(Comment)
	# likes = models.ManyToManyField(User, null=True)
	parentCardsSet = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

	class Meta:
		ordering = ('created_at',)
		verbose_name = 'Набор флеш-карт'
		verbose_name_plural = 'Наборы флеш-карт'
   

class Card(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cardsSet = models.ForeignKey(CardsSet, on_delete=models.SET_NULL, null=True)
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = 'Флеш-карта'
        verbose_name_plural = 'Флеш-карты'


class Favorite(models.Model): #fk
	user = models.ForeignKey(User, on_delete=models.CASCADE);
	set = models.ForeignKey(CardsSet, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Избранное'
		verbose_name_plural = 'Избранные наборы флеш-карт'

  


