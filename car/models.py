from django.db import models
from car_brand.models import Brand
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    image = models.ImageField(upload_to='car/media/uploads/')
    car_brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    buyer = models.ManyToManyField(User)
    in_stock = models.IntegerField(null=True, blank=True)
    car_name = models.CharField(max_length=50)
    price = models.CharField(max_length=8)
    details = models.TextField()
    
    def __str__(self):
        return self.car_name+ ' '+ self.car_brand.brand_name