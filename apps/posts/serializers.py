# serializers.py
from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude =[]

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        exclude =[]

    def create(self, validated_data):
        comments_data = validated_data.pop('comments', [])  # Remove comments from the validated_data
        post_instance = Post.objects.create(**validated_data)

        # Create comments related to the post
        for comment_data in comments_data:
            Comment.objects.create(post=post_instance, **comment_data)

        return post_instance
