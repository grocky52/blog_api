from rest_framework import serializers
from .models import Post, Category


class postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')


class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']
