from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    role = models.CharField(max_length=32)

    def __unicode__(self):
        str1 = self.name + " | " + self.password + " | " + self.role
        return str1


class Role(models.Model):
    name = models.CharField(max_length=32)
    authority = models.CharField(max_length=128)

    def __unicode__(self):
        str1 = self.name + " | " + self.authority
        return str1


class Inception(models.Model):
    address = models.CharField(max_length=32)
    port = models.IntegerField()
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    isSelected = models.IntegerField()
