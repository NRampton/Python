from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.

NAME_REGEX = re.compile(r'^[^a-zA-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def uni_str_dict(mydict):
    data = {}
    for key, value in mydict.iteritems():
        data[key] = str(value)
    return data


class UserManager(models.Manager):
    def createUser(self, form):
        flag = False
        errors = {}
        data = uni_str_dict(form)
        if len(data['first_name']) < 2:
            flag = True
        if len(data['last_name']) < 2:
            flag = True
            errors['last_name_length'] = "Your last name must be at least two characters long."
        for char in range(len(data['first_name'])):
            if NAME_REGEX.match(data['first_name'][char]):
                errors['first_name_number'] = "No numbers are allowed in first names."
                flag = True
                break
        for char in range(len(data['last_name'])):
            if NAME_REGEX.match(data['last_name'][char]):
                errors['last_name_number'] = "No numbers are allowed in last names."
                flag = True
                break
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "We're going to need a valid email address."
            flag = True
        if not data['password'] == data['confirm_password']:
            errors['password'] = "Password does not match."
            flag = True
        if flag:
            return (False, errors)
        new_user = self.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=bcrypt.hashpw(data['password'].encode, bcrypt.gensalt()))
        return (True, new_user)

    def login(self, form):
        flag = False
        errors = {}
        data = uni_str_dict(form)
        called_user = User.manager.get(email=data['email'])
        if not called_user['email']:
            flag = True
            errors['email'] = "That email is not found in our records"
        if not called_user['password'] == bcrypt.hashpw(data['password'].encode, bcrypt.gensalt()):
            flag = True
            errors['password'] = "That password is incorrect. Forgot your password? Sorry, haven't learned what to do about that yet."
        if flag:
            return (False, errors)
        return (True, called_user)




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = UserManager()
