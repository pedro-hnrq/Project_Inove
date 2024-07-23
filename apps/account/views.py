from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from utils.jsonplaceholder import get_users
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

    def list(self, request):
        users = get_users()
        for user in users:
            User.objects.get_or_create(id=user['id'], name=user['name'], username=user['username'], email=user['email'])
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
