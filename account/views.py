from django.shortcuts import render
#'.'은 같은 파일을 뜻함
from .models import User

def login(request):
    return render(request, 'account/login.html')


############여기하다말음, 회원가입 404
"""
def join(request):
    name = request.data.get('name', None)
    birthdate = request.data.get('birthdate', None)
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    join_date = request.data.get('join_date', None)

    User.objects.create(name=name,
                        birthdate=birthdate,
                        email=email,
                        password=password,
                        join_date=join_date
                        )
    return render(request, 'account/join.html')
    """


def profile(request):
    return render(request, 'account/profile.html')