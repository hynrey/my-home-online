from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Entity(models.Model):
    modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='modified_by_solution1')
    value = models.IntegerField(blank=True, null=True)
    properties = models.ManyToManyField('Property')


class Property(models.Model):
    key = models.CharField(blank=True, null=True, max_length=250)
    value = models.CharField(blank=True, null=True, max_length=250)
