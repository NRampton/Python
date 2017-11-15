from __future__ import unicode_literals

from django.db import models

# Create your models here.


def uni_str_dict(mydict):
    data = {}
    for key, value in mydict.iteritems():
        data[key] = str(value)
    return data


class CourseManager(models.Manager):
    def create_new_course(self, form):
        flag = False
        errors = {}
        data = uni_str_dict(form)
        print data
        if len(data['name']) < 5:
            flag = True
            errors['name'] = "Your course name must be at least five characters long."
        if len(data['desc']) < 15:
            flag = True
            errors['desc'] = "Your course description must be at least fifteen characters long."
        if flag:
            return (False, errors)
        course = self.create(name=data['name'], desc=data['name'])
        return (True, course)


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    manager = CourseManager()
    objects = models.Manager()


class Desc(models.Model):
    desc = models.CharField(max_length=255)
    course_described = models.OneToOneField(Course, related_name='course_desc')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
