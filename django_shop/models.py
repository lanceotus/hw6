from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='img')
    blade_material = models.CharField(max_length=255)
    hardness = models.CharField(max_length=10)
    handle_material = models.CharField(max_length=255)
    lock = models.CharField(max_length=50)
    action = models.CharField(max_length=255)
    blade_length = models.DecimalField(max_digits=15, decimal_places=2)
    full_length = models.DecimalField(max_digits=15, decimal_places=2)
    blade_thickness = models.DecimalField(max_digits=15, decimal_places=2)
    weight = models.DecimalField(max_digits=15, decimal_places=2)
    producer = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
