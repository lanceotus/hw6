from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    blade_material = models.CharField(max_length=255)
    hardness = models.CharField(max_length=10)
    handle_material = models.CharField(max_length=255)
    lock = models.CharField(max_length=50)
    action = models.CharField(max_length=255)
    blade_length = models.FloatField()
    full_length = models.FloatField()
    blade_thickness = models.FloatField()
    weight = models.FloatField()
    producer = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name}'
