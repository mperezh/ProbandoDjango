from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):

    def __init__(self):
        title = models.CharField()
        body = models.TextField()
        date = models.DateTimeField()


    def __str__(self):
        return self.title
