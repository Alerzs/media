from rest_framework.serializers import ModelSerializer
from .models import SocialUser , Post


class SocialSerializer(ModelSerializer):
    class Meta:
        model = SocialUser
        fields = ['followers']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        exclude = ['user']