from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.IntegerField()
    user_id = models.IntegerField()