from django.urls import path

from.import views

#이곳은 메인페이지로 메뉴 등등을 띄우면 됨
urlpatterns = [
    path('login/',views.login),
    path('join/',views.join),
    path('profile/',views.profile),
]