from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    #birth_date = forms.DateField()
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")  # "birth_date" 필드 추가