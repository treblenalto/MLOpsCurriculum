from django.test import TestCase
from rest_framework import serializers

from .models import User
from .serializers import UserSerializer


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="Testzero", age=20)
        User.objects.create(name="Testone", age=21)

    # get all users
    def test_get_user_list(self):
        response = User.objects.all()
        self.assertEqual(len(response), 2)

    # get a user
    def test_get_user_detail(self):
        response = User.objects.get(name="Testzero")
        self.assertEqual(response.name, "Testzero")
        self.assertEqual(response.age, 20)

    # get a user with invalid id
    def test_get_user_detail_invalid_id(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=-1)

    # create a user
    def test_post_user(self):
        User.objects.create(name="Testtwo", age=23)
        Newuser = User.objects.get(name="Testtwo")
        self.assertEqual(Newuser.name, "Testtwo")
        self.assertEqual(Newuser.age, 23)

    # create a user with no age - nullable
    def test_post_user_no_age(self):
        User.objects.create(name="Testthree")
        Newuser = User.objects.get(name="Testthree")
        self.assertEqual(Newuser.name, "Testthree")
        self.assertEqual(Newuser.age, None)

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
    def test_update_user(self):
        Testzero = User.objects.get(name="Testzero")
        Testzero.name = "UpdatedName"
        Testzero.age = 20
        Testzero.save()
        self.assertEqual(Testzero.name, "UpdatedName")
        self.assertEqual(Testzero.age, 20)

    # update a user with invalid id
    def test_update_user_invalid_id(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=-1)

    # delete a user
    def test_delete_user(self):
        Testzero = User.objects.get(name="Testzero")
        Testzero.delete()
        self.assertRaises(User.DoesNotExist)

    # delete a user with invalid id
    def test_delete_user_invalid_id(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=-1)
