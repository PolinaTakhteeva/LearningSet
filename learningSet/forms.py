from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    
    class Meta:
        fields = (User.username.field_name, User.password.field_name)
        model = User