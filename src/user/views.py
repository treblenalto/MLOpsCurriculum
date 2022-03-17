# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # SELECT * FROM User
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"success": True, "message": "User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        objects = User.objects.get(id=kwargs["pk"])
        serializer = UserSerializer(objects, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"success": True, "message": "User updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        objects = User.objects.get(id=kwargs["pk"])
        objects.delete()
        return Response({"success": True, "message": "User deleted successfully"}, status=status.HTTP_200_OK)
