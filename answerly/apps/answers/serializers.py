from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Answer
        fields = '__all__'