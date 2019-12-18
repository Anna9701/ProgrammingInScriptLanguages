from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Lecturer(models.Model):
    name = models.CharField(max_length=40)
    website = models.URLField()


class Student(models.Model):
    name = models.CharField(max_length=40)


class Lecture(models.Model):
    name = models.CharField(max_length=140)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
