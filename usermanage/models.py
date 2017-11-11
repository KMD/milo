import random

from django.contrib.auth.models import AbstractUser, models

class MyUser(AbstractUser):
    birthday = models.DateField(null=True)
    randomNumber = models.IntegerField(default=random.randint(0,100))
