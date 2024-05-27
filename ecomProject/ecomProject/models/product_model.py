from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    # class Meta:
    #     abstract = True


class DairyProduct(Product):

    expiration_date = models.DateField(
        auto_now=False, auto_now_add=True
    )

    class Meta:
        db_table = 'dairy_product'
