from django.db import models


class Algorithm(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200)
