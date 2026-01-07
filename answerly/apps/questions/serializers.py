from rest_framework import serializers
from .models import Question
from apps.votes.models import Vote
from django.contrib.contenttypes.models import ContentType
from apps.tags.serializers import TagSerializer
from apps.tags.models import Tag

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

    tag = serializers.ListField(
        child = serializers.CharField(),
        write_only=True,
    )

    tag_objects = TagSerializer(many=True, read_only=True, source='tags')

    class Meta:
        model = Question
        fields = [
        "id",
        "author",
        "upvotes",
        "downvotes",
        "tag_objects",
        "tag",
        "title",
        "body",
        "created_at",
        "updated_at",
    ]

    def create(self, validated_data):
        tags_data = validated_data.pop('tag', [])
        question = Question.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name.lower())
            question.tags.add(tag)

        return question

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tag', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if tags_data:
            instance.tags.clear()
            for tag_name in tags_data:
                tag, created = Tag.objects.get_or_create(name=tag_name.lower())
                instance.tags.add(tag)

        return instance

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