from projectapp.models import Project
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='subscription')
    objects = models.Manager()

    class Meta:
        unique_together = ('user', 'project')
