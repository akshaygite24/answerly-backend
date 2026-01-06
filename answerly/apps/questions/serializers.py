from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Question
        fields = '__all__'