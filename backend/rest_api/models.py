from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title + " " + self.description


class Link(models.Model):
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category')

