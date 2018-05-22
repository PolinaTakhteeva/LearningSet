
from django.contrib import admin
from django.urls import path, include
from learningSet import views
from django.conf import settings
from django.conf.urls.static import static
from learningSet.views import CardsSetCreate, CardsSetUpdate, CardsSetDelete, CardCreate, CardUpdate, CardDelete


urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('cardsSet_create/', views.cardsSet_create, name='cardsSet_create'),

    path('card/add/<int:set_id>/', CardCreate.as_view(), name='card_add'),
    path('card/<int:pk>/', CardUpdate.as_view(), name='card_update'),
    path('card/<int:pk>/delete/', CardDelete.as_view(), name='card_delete'),
    path('card_create/', views.card_create, name='card_create'),

    path('login/', views.login, name='login'),
    path('like/', views.like, name='like'),
    path('api/users/list/', views.users_list_api, name='users_list_api')
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
