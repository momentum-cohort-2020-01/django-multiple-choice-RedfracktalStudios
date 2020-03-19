from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
