from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post