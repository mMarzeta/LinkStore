from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title + " " + self.description


class Link(models.Model):
    url = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='links')
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.url + " " + str(self.category) + " " + self.description
