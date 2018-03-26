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
	except User.DoesNotExist:
		raise Http404
	return render(
		request, 'learningSet/user_detail.html',
		{'user': user}
		)

def cardsSets_list(request):
	sets = CardsSet.objects.all()[:10]
	return render(
		request, 'learningSet/users_list.html',
		{'sets': sets}
		)	

def my_cardsSets_list(request):
	my_sets = CardsSet.objects.all()[:10]


def cardSet(request):
	set = Card. object.all()[:5]
	return render(
		request, 'learningSet/cardSet_detail.html',
		)



def card(request, pk):
      try:
          object = Card.objects.get(pk=pk)
      except Post.DoesNotExist:
          raise Http404
      return render(
           request, 'blog/post_detail.html',
           {'object': object}
      )
