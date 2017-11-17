from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def createUser(self, form):



class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()

    def __str__.(self):
        return "User #{}, Name: {} {}, email: {}".format(self.id, self.name, self.alias, self.email)
