from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def mainpage(request):
    #여기다가 mymail/PrevLetter.object 가져오면 됨
    return render(request, 'pages/mainpage.html')
def aroseagida(request):
    return render(request, 'pages/aroseagida.html')
def raonhaje(request):
    return render(request, 'pages/raonhaje.html')

def test(request):
    return render(request, 'pages/test.html')

def company(request):
    return render(request, 'pages/company_info.html')

