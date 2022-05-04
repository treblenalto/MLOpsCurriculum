# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # SELECT * FROM User
    serializer_class = UserSerializer
    
    # return id, name, age of deleted user
    def destroy(self, request, *args, **kwargs):
        objects = User.objects.get(id=kwargs["pk"])
        serialized = UserSerializer(objects).data
        objects.delete()
        return Response(serialized)