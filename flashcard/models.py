from django.db import models
from users.models import User


class Flashcard(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
  

    def __str__(self):
      return self.title


