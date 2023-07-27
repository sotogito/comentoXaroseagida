from django.db import models

class subscription_product(models.Model):
    #mail_num = ArrayField(models.IntegerField()) #정수형배열, 중복판별
        #=> ArrayField로 배열을 저장하고 싶으면 PostgreSQL이 필요함. psycopg2깔아야함.
    name = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)