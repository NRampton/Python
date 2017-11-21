from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
from django import forms
import re

NAME_REGEX = re.compile(r"^[^a-zA-z'\u00C0-\u00D6]$")
# Create your models here.


def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than two.'.format(value)
        )


def validateNoNumerals(value):
    for char in range(len(value)):
        if NAME_REGEX.match(value[char]):
            raise ValidationError(
                '{} may not contain numerals.'.format(value)
            )


class User(models.Model):
    first_name = models.CharField(max_length=255, validators=[validateLengthGreaterThanTwo, validateNoNumerals])
    last_name = models.CharField(max_length=255, validators=[validateLengthGreaterThanTwo, validateNoNumerals])
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
