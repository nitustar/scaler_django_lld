from django.db import models


class User(models.Model):
    title = models.CharField(max_length=100, choices=[("Mr", "Mr"), ("Mrs", "Mrs"), ("Miss", "Miss")])
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)

