from django.db import models
from django.conf import settings
from apps.tags.models import Tag

# Create your models here.
User = settings.AUTH_USER_MODEL

class Question(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)

    def __str__(self):
        return self.title