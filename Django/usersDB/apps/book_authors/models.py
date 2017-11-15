from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Author #{}: {} {}, email: {}>".format(self.id, self.first_name, self.last_name, self.email)


class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return "<Book #{} name: {}, description: {}>".format(self.id, self.name, self.desc)
