# from django.shortcuts import render
from rest_framework import viewsets
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
            return Response({"success": True, "message": "User created successfully"})
        else:
            return Response({"success": False, "message": serializer.errors})

    def update(self, request, *args, **kwargs):
        objects = User.objects.get(id=kwargs["pk"])
        serializer = UserSerializer(objects, data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response({"success": True, "message": "User updated successfully"})
        else:
            return Response({"success": False, "message": serializer.errors})

    def destroy(self, request, *args, **kwargs):
        objects = User.objects.get(id=kwargs["pk"])
        objects.delete()
        return Response({"success": True, "message": "User deleted successfully"})

