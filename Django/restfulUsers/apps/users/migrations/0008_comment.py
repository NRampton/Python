# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-20 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20171120_1658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.Message')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.User')),
            ],
        ),
    ]
