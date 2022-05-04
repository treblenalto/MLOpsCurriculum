from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import serializers, exceptions
from rest_framework.test import APIRequestFactory

from user.models import User
from user.views import UserViewSet
from user.serializers import UserSerializer


class UserViewTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Testzero", age=20)
        User.objects.create(name="Testone", age=21)

    # create a user with no age - nullable
    def test_post_user_no_age(self):
        request = APIRequestFactory().post(
            reverse_lazy("user-list"), {"name": "Testthree"}
        )
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

    # delete a user
    def test_delete_user(self):
        Testone = User.objects.get(name="Testone")
        request = APIRequestFactory().delete(
            reverse_lazy("user-detail", args=[Testone.id])
        )
        view = UserViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=Testone.id)
        self.assertEqual(response.status_code, 200)
