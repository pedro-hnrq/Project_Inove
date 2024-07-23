from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # extra_kargs = {
        #     'date_modif': {'white_only': True}
        # }
        fields = ('id', 'userId', 'title', 'body')

# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'