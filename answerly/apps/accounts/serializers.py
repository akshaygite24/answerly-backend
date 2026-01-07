from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    joined = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('username', 'reputation', 'joined')

    def get_joined(self, obj):
        return obj.user.date_joined.strftime('%B %Y')