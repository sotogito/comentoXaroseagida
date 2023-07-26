from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    name = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    join_date = models.DateTimeField(auto_now_add=True)