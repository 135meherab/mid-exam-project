from django.db import models
from car.models import Car

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    email= models.EmailField(max_length=100)
    commnet = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)