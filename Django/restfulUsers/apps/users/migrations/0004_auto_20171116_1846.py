# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-16 18:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171116_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relationship',
            name='user',
        ),
        migrations.RemoveField(
            model_name='relationship',
            name='user2',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]