from django.db import models


class User(models.Model):
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)

    # projects = models.ManyToManyField("Project", blank=True, related_name="projects")

    def __str__(self):
        return "{}".format(self.email)


class Project(models.Model):
    name = models.CharField(max_length=150)
    developer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.name)
