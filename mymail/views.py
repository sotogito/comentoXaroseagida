from django.shortcuts import render
from .models import PrevLetter


def mymail(request):
    active_count = PrevLetter.objects.filter(is_active=True).count()
    question_list = PrevLetter.objects.order_by('-id').filter(is_active=True)
    question_context = {
        'question_list' : question_list ,
        'active_count': active_count
    }
    return render(request, 'mymail/mymail.html',question_context)

def blockmail(request):
    return render(request, 'mymail/blockmail.html')
