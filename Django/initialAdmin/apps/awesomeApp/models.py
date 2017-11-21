from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Fruit(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField()
    color = models.CharField(max_length=50)


class Donut(models.Model):
    flavor = models.CharField(max_length=255)
    price = models.IntegerField()


class Group(models.Model):
    name = models.CharField(max_length=50)
    membership = models.IntegerField
