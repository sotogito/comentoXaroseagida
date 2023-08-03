from django.urls import path

from.import views

#이곳은 메인페이지로 메뉴 등등을 띄우면 됨
urlpatterns = [
    path('mymail/',views.mymail),
    path('mymail/blockmail/',views.blockmail, name='myletter_blockmail'),
    #데이터 받기
    path('api/receive_unity_data/', views.receive_unity_data, name='receive_unity_data'),
]
