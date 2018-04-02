from django.shortcuts import render
from django.http import Http404
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from learningSet.models import Card, CardsSet, Favorite
from learningSet.forms import LoginForm

def users_list(request):
	users = User.objects.all()[:20]
	return render(
		request, 'learningSet/users_list.html',
		{'users': users}
		)

def user_detail(request, user_id):
	try:
		user = User.objects.get(id=user_id)
		sets = CardsSet.objects.filter(creator=user_id)[:10]
	except User.DoesNotExist:
		raise Http404
	return render(
		request, 'learningSet/user_detail.html',
		{'user': user, 'sets': sets}
		)

def cardsSets_list(request):
	sets = CardsSet.objects.all()[:10]
	return render(
		request, 'learningSet/cardsSet_list.html',
		{'sets': sets}
		)

def cardsSet_detail(request, set_id):
	try:
		set = CardsSet.objects.get(id=set_id)
		likes = Favorite.objects.filter(set=set_id).count()
		cards =Card.objects.filter(cardsSet=set_id)[:20]
	except CardsSet.DoesNotExist:
		raise Http404
	return render(
		request, 'learningSet/cardsSet_detail.html',
		{'set': set, 'cards': cards, 'likes': likes}
		)


def card_detail(request, card_id):
      try:
          card = Card.objects.get(id=card_id)
      except Card.DoesNotExist:
          raise Http404
      return render(
           request, 'learningSet/card_detail.html',
           {'card': card}
      )


def login(request):
    if request.method == 'POST':
    	form = LoginForm(request.POST)
    	username = request.POST['username']
    	password = request.POST['password']
    	user = authenticate(username=username, password=password)
    	if user is not None:
        	auth_login(request, user)
        	sets = CardsSet.objects.all()[:10]
        	return render(
				request, 'learningSet/cardsSet_list.html',
				{'sets': sets, 'username': username}
				)
    else:
    	form = LoginForm()
    return render(
        request, 'login.html',
        {'form': form }
    )
