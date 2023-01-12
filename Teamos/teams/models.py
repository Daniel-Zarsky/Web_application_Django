__author__ = "Samuel Simun - xsimun04@fit.vutbr.cz"

from django.db import models

class Teams_list(models.Model):
    name = models.CharField(max_length=100)
    members = models.TextField(null=True)
    projects = models.TextField(null=True)
    invited = models.TextField(null=True)
    img = models.ImageField(upload_to="media/")
    owner = models.CharField(max_length=100)
