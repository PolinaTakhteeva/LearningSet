from django.contrib.auth.models import User
from random_words import RandomWords
import names

rw = RandomWords()
name = names.get_full_name();
un = name.replace(" ", "")
pw = rw.random_word() + rw.random_word()
user = User(username=un, password=pw, first_name=name.split(" ", 1)[0], last_name=name.split(" ", 1)[1], email = un+"@mail.com")
user.save()
