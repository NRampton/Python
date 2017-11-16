# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-16 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_relationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='user',
        ),
        migrations.AddField(
            model_name='relationship',
            name='user',
            field=models.ManyToManyField(related_name='relationships', to='users.User'),
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='user2',
        ),
        migrations.AddField(
            model_name='relationship',
            name='user2',
            field=models.ManyToManyField(related_name='relationships2', to='users.User'),
        ),
    ]