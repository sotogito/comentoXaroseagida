from django.shortcuts import render
from .models import PrevLetter

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PrevLetterSerializer



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

####################################
@api_view(['POST'])
def receive_unity_data(request):
    serializer = PrevLetterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_prev_letters(request):
    prev_letters = PrevLetter.objects.all()
    serializer = PrevLetterSerializer(prev_letters, many=True)
    return Response(serializer.data)


