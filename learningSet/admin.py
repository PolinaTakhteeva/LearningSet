from django.contrib import admin
from learningSet.models import Card, CardsSet, Comment, UserProfile

# Register your models here.
admin.site.register(Card)
admin.site.register(CardsSet)
admin.site.register(Comment)
admin.site.register(UserProfile)
