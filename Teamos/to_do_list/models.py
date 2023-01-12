__author__ = "Daniel Zarsky - xzarsk04@fit.vutbr.cz"

from django.db import models

# Create your models here.
class Task(models.Model):

    project= models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=False)
    deadline = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()

    def _str_(self):
         return self.title

    class Meta:
         ordering = ['priority']

