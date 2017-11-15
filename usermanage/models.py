import random

from django.contrib.auth.models import AbstractUser, models


class MyUser(AbstractUser):
    birthday = models.DateField(null=True)
    random_number = models.IntegerField(default=random.randint(0, 100))

    def get_absolute_url(self):
        return u'/user/%d' % self.id
