from __future__ import unicode_literals
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User #{}, Name: {} {}".format(self.id, self.first_name, self.last_name)


class Friendship(models.Model):
    user = models.ForeignKey(User, related_name="friend")
    friend = models.ForeignKey(User, related_name="user")

    def __str__(self):
        return "Yay, {} is friends with {}!".format(self.user, self.friend)
