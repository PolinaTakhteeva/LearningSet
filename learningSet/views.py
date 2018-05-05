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
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def welcome(request):
	return render(
		request, 'learningSet/welcome_ex.html',
		)

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
        set_id = request.POST.get('set_id', None)
        set = CardsSet.objects.get(id=set_id)
        if not Favorite.objects.filter(set=set_id, user=user):
        	like = Favorite(user=user, set = set)
        	like.save()
        	status = 1
        	message = 'Cards set was added to Favorites sets'
        else:
        	Favorite.objects.filter(set=set_id, user=user).delete()
        	set.likes_count-=1
        	message = 'Cards set was removed from Favorites sets'
        	status = 0
        set.save()
    likes = Favorite.objects.filter(set=set_id).count()
    ctx = {'message': message, 'likes': likes, 'status': status}
    return HttpResponse(json.dumps(ctx), content_type='application/json')


# Create & Edit Cards Sets forms

class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
                'message' : 'It is adjax'
            }
            return JsonResponse(data)
        else:
            return response

class CardsSetCreate(AjaxableResponseMixin, CreateView):
    model = CardsSet
    fields = ['name', 'description', 'educational_material', 'creator']


@login_required
@require_POST
def cardsSet_create(request):
    if request.method == 'POST':
    	#Get creator
        user = request.user
        message = "lalala"

    ctx = {'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')

class CardsSetUpdate(UpdateView):
    model = CardsSet
    fields = ['name']

class CardsSetDelete(DeleteView):
    model = CardsSet
    success_url = reverse_lazy('sets_list')









