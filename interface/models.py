from django.db import models


class Trajectory(models.Model):
    trajectory = models.TextField(max_length=200)
