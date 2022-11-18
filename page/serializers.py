from rest_framework import serializers
from .models import Article

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id', 'title', 'summary', 'author', 'body', 'created', 'updated', 'image'
        )
        model = Article

