from django.db import models
from django.conf import settings
from apps.questions.models import Question

User = settings.AUTH_USER_MODEL

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='answers'
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Answer by {self.author} on Question {self.question.id}'

