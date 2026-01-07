from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from apps.votes.models import Vote
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = [
            "id",
            "question",
            "author",
            "body",
            "upvotes",
            "downvotes",
            "created_at",
            "updated_at",
        ]

    def get_upvotes(self, obj):
        content_type = ContentType.objects.get_for_model(Answer)
        return Vote.objects.filter(
            content_type=content_type,
            object_id=obj.id,
            value=1
        ).count()
    
    def get_downvotes(self, obj):
        content_type = ContentType.objects.get_for_model(Answer)
        return Vote.objects.filter(
            content_type=content_type,
            object_id=obj.id,
            value=-1
        ).count()