from django.shortcuts import render
from .models import PrevLetter
from django.contrib.auth.decorators import login_required

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

#############unity##############
'''
@api_view(['POST'])
def receive_unity_data(request):
    serializer = PrevLetterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
'''
@login_required(login_url='accounts:login')
@api_view(['GET'])
def get_prev_letters(request):
    PrevLetter.author = request.user  # 현재 로그인한 사용자
    prev_letters = PrevLetter.objects.all(owner=PrevLetter.author)
    serializer = PrevLetterSerializer(prev_letters, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def receive_unity_data(request):
    serializer = PrevLetterSerializer(data=request.data)

    if serializer.is_valid():
        received_data = serializer.validated_data
        question_type = received_data['question_type']
        level_type = received_data['level_type']
        question = received_data['question']
        option = received_data['option']

        # 중복 판별 로직
        if PrevLetter.objects.filter(
            question_type=question_type,
            level_type=level_type,
            question=question,
            option=option,
        ).exists():
            return Response({'message': 'Duplicate data'}, status=400)

        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)
