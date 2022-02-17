from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Family(models.Model):
    join_data = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family = models.OneToOneField(Family, on_delete=models.SET_NULL, null=True)
    nickname = models.TextField()





