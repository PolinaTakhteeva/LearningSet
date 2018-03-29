"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from learningSet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cardsSets_list, name='welcome'),
    path('users/list/', views.users_list, name='users_list'),
    path(
        'users/<int:user_id>/',
        views.user_detail, name='user_detail'),
    path(
        'cardsSet_detail/<int:set_id>/',
        views.cardsSet_detail, name='set_detail'),
    path(
        'card_detail/<int:card_id>/',
        views.card_detail, name='card_detail'),
    path('login/', views.login, name='login')

]
