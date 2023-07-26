from django.shortcuts import render

# Create your views here.


#화면에 가져오기
#django파일에서 shortcuts을 가져옴
from django.shortcuts import render
#'.'은 같은 파일을 뜻함
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    return render(request, 'mysite/content_list.html',context)








