from rest_framework import viewsets, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    def list(self, request):
        response = requests.get(f'{BASE_URL}/posts')
        posts_data = response.json()
        for post in posts_data:
            if not Post.objects.filter(id=post['id']).exists():
                Post.objects.create(
                    id=post['id'],
                    userId_id=post['userId'],
                    title=post['title'],
                    body=post['body']
                )
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        post_data = request.data
        response = requests.post(f'{BASE_URL}/posts', json=post_data)
        post = response.json()
        Post.objects.create(
            id=post['id'],
            userId_id=post['userId'],
            title=post['title'],
            body=post['body']
        )
        return Response(post, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        post_data = request.data
        response = requests.put(f'{BASE_URL}/posts/{pk}', json=post_data)
        if response.status_code == 200:
            post = response.json()
            Post.objects.filter(id=pk).update(
                title=post['title'],
                body=post['body'],
                userId_id=post['userId']
            )
            return Response(post, status=status.HTTP_200_OK)
        else:
            return Response(response.json(), status=response.status_code)

    def destroy(self, request, pk=None):
        response = requests.delete(f'{BASE_URL}/posts/{pk}')
        if response.status_code == 200:
            Post.objects.filter(id=pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(response.json(), status=response.status_code)
