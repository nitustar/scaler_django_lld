from django.db import models


class Product(models.Model):
    seller = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()
