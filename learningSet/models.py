from django.db import models

# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    created_date = models.DateTimeField('created date')