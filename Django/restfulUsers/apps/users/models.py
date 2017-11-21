from __future__ import unicode_literals
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User #{}, Name: {}".format(self.id, self.name)


class Friendship(models.Model):
    user = models.ForeignKey(User, related_name="friends")
    friend = models.ForeignKey(User, related_name="users")

    def __str__(self):
        return "Yay, {} is friends with {}!".format(self.user, self.friend)


class Message(models.Model):
    content = models.CharField(max_length=75)
    user = models.ForeignKey(User, related_name="messages")

    def __str__(self):
        return "Message #{}, posted by {}".format(self.id, self.user.name)


class Comment(models.Model):
    content = models.CharField(max_length=50)
    message = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")

    def __str__(self):
        return "Comment #{}, made by {}".format(self.id, self.user.name)
