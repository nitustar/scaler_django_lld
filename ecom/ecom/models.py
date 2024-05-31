from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # shipping_address = models.TextField()
    # billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    default_shipping_address = models.ForeignKey("ShippingAddress",
                                                 on_delete=models.DO_NOTHING,
                                                 null=True,
                                                 related_name="user_info"
                                                 )

    def __str__(self):
        return self.name


class Address(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        abstract = True


class ShippingAddress(Address):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_address")
