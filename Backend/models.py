from django.db import models


class User(models.Model):
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return "{}".format(self.name)


class Project(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return "{}".format(self.name)
