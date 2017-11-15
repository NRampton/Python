from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: id: {} name: {} {}, age: {}>".format(self.id, self.first_name, self.last_name, self.age)


    # some sort of validation would be included via a full_clean() method built into Django's
    # Model instance handler. That's where to look for more info here.
