from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_logout_time = models.DateTimeField(null=True,blank=True)

