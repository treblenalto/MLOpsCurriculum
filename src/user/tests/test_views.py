from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from user.models import User
from user.views import UserViewSet
from user.serializers import UserSerializer


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Testzero", age=20)
        User.objects.create(name="Testone", age=21)

    # get all users
    def test_get_user_list(self):
        request = APIRequestFactory().get(reverse_lazy("user-list"))
        view = UserViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        
    # get a user
    def test_get_user_detail(self):
        Testzero = User.objects.get(name="Testzero")
        request = APIRequestFactory().get(reverse_lazy("user-detail", args=[Testzero.id]))
        view = UserViewSet.as_view({"get": "retrieve"})
        response = view(request, pk=Testzero.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Testzero")
        self.assertEqual(response.data["age"], 20)

    # get a user with invalid id
    def test_get_user_detail_invalid_id(self):
        request = APIRequestFactory().get(reverse_lazy("user-detail", args=[-1]))
        view = UserViewSet.as_view({"get": "retrieve"})
        response = view(request, pk=-1)
        self.assertEqual(response.status_code, 404)
        
    # create a user
    def test_post_user(self):
        request = APIRequestFactory().post(reverse_lazy("user-list"), {"name": "Testtwo", "age": 23})
        view = UserViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.get(name="Testtwo").age, 23)

    # create a user with no age - nullable
    def test_post_user_no_age(self):
        request = APIRequestFactory().post(reverse_lazy("user-list"), {"name": "Testthree"})
        view = UserViewSet.as_view({"post": "create"})
        response = view(request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.get(name="Testthree").age, None)

    # create a user with negative age
    def test_post_user_negative_age(self):
        with self.assertRaisesMessage(
            serializers.ValidationError, "Age must be positive"
        ):
            serializer = UserSerializer(data={"name": "Testfive", "age": -1})
            serializer.is_valid(raise_exception=True)
            
    # create a user with no name
    def test_post_user_no_name(self):
        with self.assertRaisesMessage(
            serializers.ValidationError, "This field is required."
        ):
            serializer = UserSerializer(data={"age": 23})
            serializer.is_valid(raise_exception=True)
            
    # update a user
    def test_put_user(self):
        Testone = User.objects.get(name="Testone")
        request = APIRequestFactory().put(reverse_lazy("user-detail", args=[Testone.id]), {"name": "Testone", "age": 30})
        view = UserViewSet.as_view({"put": "update"})
        response = view(request, pk=Testone.id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.get(name="Testone").age, 30)

    # update a user with invalid id 
    def test_put_user_invalid_id(self):
        request = APIRequestFactory().put(reverse_lazy("user-detail", args=[-1]), {"name": "Testone", "age": 30})
        view = UserViewSet.as_view({"put": "update"})
        response = view(request, pk=-1)
        self.assertEqual(response.status_code, 404)
        
    # delete a user
    def test_delete_user(self):
        Testone = User.objects.get(name="Testone")
        request = APIRequestFactory().delete(reverse_lazy("user-detail", args=[Testone.id]))
        view = UserViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=Testone.id)
        self.assertEqual(response.status_code, 200)
    
    def test_delete_user_invalid_id(self):
        request = APIRequestFactory().delete(reverse_lazy("user-detail", args=[-1]))
        view = UserViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=-1)
        self.assertEqual(response.status_code, 404)