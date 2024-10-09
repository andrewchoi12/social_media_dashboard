from rest_framework import serializers
from .models import SocialMediaPost

class SocialMediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPost
        fields = ['id', 'platform', 'post_id', 'content', 'likes', 'comments', 'shares', 'timestamp', 'sentiment_score']