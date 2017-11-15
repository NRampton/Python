from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Dojo(models.Model):
    name = models.CharField(max_length=75)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=50)
    desc = models.TextField()

    def __repr__(self):
        return "<Dojo #{}: {} in {}, {}. {}>".format(self.id, self.name, self.city, self.state, self.desc)


class Ninja(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __repr__(self):
        return "<#{}: name: {} {}, studies at Dojo #{}>".format(self.id, self.first_name, self.last_name, self.dojo)
