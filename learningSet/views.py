from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from learningSet.models import Card, CardsSet, Favorite
from learningSet.forms import LoginForm
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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
	set = CardsSet.objects.get(id=set_id)
	likes = Favorite.objects.filter(set=set_id).count()
	cards = Card.objects.filter(cardsSet=set_id)[:20]
	username = None
	try:
		if request.user.is_authenticated:
			user = request.user
	except CardsSet.DoesNotExist:
		raise Http404
	return render(
		request, 'learningSet/cardsSet_detail.html',
		{'set': set, 'likes': likes, 'cards': cards, 'user': user}
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


@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        user = User.objects.get(id=user.id)
        set_id = request.POST.get('set_id', None)
        set = CardsSet.objects.get(id=set_id)
        if not Favorite.objects.filter(set=set_id, user=user):
        	like = Favorite(user=user, set = set)
        	like.save()
        	status = 1
        	message = 'Cards set was added to Favorites sets'
        else:
        	Favorite.objects.filter(set=set_id, user=user).delete()
        	message = 'Cards set was removed from Favorites sets'
        	status = 0
    likes = Favorite.objects.filter(set=set_id).count()
    ctx = {'message': message, 'likes': likes, 'status': status}
    return HttpResponse(json.dumps(ctx), content_type='application/json')
