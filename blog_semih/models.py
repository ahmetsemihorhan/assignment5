from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from tags.models import Tag
# Create your models here.

class Blogx(models.Model):

    namex = models.CharField(max_length=220)
    descriptionx = models.CharField(max_length=520)
    ownerx = models.ForeignKey(User)
    tagsx = models.ManyToManyField(Tag)