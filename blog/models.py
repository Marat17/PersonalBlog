from django.db import models
from django.utils import timezone


class Mypost(models.Model):
    text = models.CharField(max_length=140)
    time = models.DateTimeField(default=timezone.now)
    header = models.CharField(max_length=15, default='No')

    def __str__(self):
        return self.text