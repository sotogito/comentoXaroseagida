from django.db import models
from django.contrib.auth.models import User
#from django.contrib.postgres.fields import ArrayField

class PrevLetter(models.Model):
    #mail_num = ArrayField(models.IntegerField()) #정수형배열, 중복판별
        #=> ArrayField로 배열을 저장하고 싶으면 PostgreSQL이 필요함. psycopg2깔아야함.
    question_type = models.IntegerField(default=0) #previousQuestions[id-1][0]
    level_type = models.IntegerField(default=0) #previousQuestions[id-1][1]
    question = models.IntegerField(default=0) #previousQuestions[id-1][2]
    option = models.IntegerField(default=0) #previousQuestions[id-1][3]
    question_text = models.CharField(max_length=200) #문자열, 이전 편지를 띄움
    is_active = models.BooleanField(default=True) #사용자가 편지 그림을 그렸는지 안그렸는지 True or False

    author = models.ForeignKey(User, on_delete=models.CASCADE)

