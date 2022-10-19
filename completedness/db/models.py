from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class pointsUser(AbstractUser):
#     # authUserId = models.ForeignKey.one_to_one
#     points = models.IntegerField()

class users(models.Model):
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    points = models.IntegerField()

        # @usersProperty
        # def getPoints():
        #     return users.objects

class workshops(models.Model):
    name = models.CharField(max_length=80)
    link = models.URLField()

class eca(models.Model):
    name = models.CharField(max_length=80)
    cost = models.IntegerField()

class connections(models.Model):
    name = models.CharField(max_length=80)
    details = models.TextField()