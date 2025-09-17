from django.db import models

# Create your models here.


class ProductModel(models.Model):
    name = models.CharField()
    price = models.FloatField()
    qty = models.IntegerField()

    def __str__(self):
        return self.name
