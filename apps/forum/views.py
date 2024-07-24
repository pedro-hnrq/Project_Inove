from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API POST - criar, listar, atualizar e deletar.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
