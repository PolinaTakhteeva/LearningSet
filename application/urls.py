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
from django.conf import settings
from django.conf.urls.static import static
from learningSet.views import CardsSetCreate, CardsSetUpdate, CardsSetDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome, name='welcome'),
    path('', views.cardsSets_list, name='sets_list'),
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
    path('set/add/', CardsSetCreate.as_view(), name='set_add'),
    path('set/<int:pk>/', CardsSetUpdate.as_view(), name='set_update'),
    path('set/<int:pk>/delete/', CardsSetDelete.as_view(), name='set_delete'),
    path('login/', views.login, name='login'),
    path('like/', views.like, name='like'),
    path('cardsSet_create/', views.cardsSet_create, name='cardsSet_create')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
