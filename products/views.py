from django.shortcuts import render


def subscribe(request):
    return render(request, 'products/subscribe.html')


