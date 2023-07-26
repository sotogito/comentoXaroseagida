from django.shortcuts import render
#'.'은 같은 파일을 뜻함
from .models import User

def login(request):
    return render(request, 'account/login.html')

def join(request):
    return render(request, 'account/join.html')

def profile(request):
    return render(request, 'account/profile.html')