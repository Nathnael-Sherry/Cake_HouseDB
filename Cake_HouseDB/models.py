import datetime

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    # email = models.EmailField()
    age = models.IntegerField()
    caketype = models.CharField(max_length=50, blank=False, null=False)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    phone = models.IntegerField()
    # gender = models.CharField(max_length=50, blank=False, null=False)
    orderdate = models.DateField(default=datetime.date.today())
    deliverydate = models.DateField(default=datetime.date.today())


def __str__(self):
    return self.name


