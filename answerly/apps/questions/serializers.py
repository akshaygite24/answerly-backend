from rest_framework import serializers
from .models import Question
from apps.votes.models import Vote
from django.contrib.contenttypes.models import ContentType

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_upvotes(self, obj):
        content_type = ContentType.objects.get_for_model(Question)
        return Vote.objects.filter(
            content_type=content_type,
            object_id=obj.id,
            value=1
        ).count()
    
    def get_downvotes(self, obj):
        content_type = ContentType.objects.get_for_model(Question)
        return Vote.objects.filter(
            content_type=content_type,
            object_id=obj.id,
            value=-1
        ).count()