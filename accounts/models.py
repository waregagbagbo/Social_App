from django.db import models
from django.forms import ModelForm
import datetime
from datetime import date


TITLE_CHOICE = [
    ('MR', 'Mr.'),
    ('MRS','Mrs'),
    ('MS','Ms'),
]

# create models

class Author(models.Model):
    fullname = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices =TITLE_CHOICE)
    country = models.CharField(max_length=50)
    residence = models.CharField(max_length=30)
    birth_date = models.DateField(blank=False, null=True)
    comments = models.TextField(blank=False)

    def __str__(self):
        return self.fullname


class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Entry(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    

        