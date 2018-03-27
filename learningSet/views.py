from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from learningSet.models import Card, CardsSet

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
		request, 'learningSet/users_list.html',
		{'sets': sets}
		)

def cardsSet_detail(request, set_id):
	try:
		set = CardsSet.objects.get(id=set_id)
		cards =Card.objects.filter(cardsSet=set_id)[:20]
	except CardsSet.DoesNotExist:
		raise Http404
	return render(
		request, 'learningSet/cardsSet_detail.html',
		{'set': set, 'cards': cards}
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
