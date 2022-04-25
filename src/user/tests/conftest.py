import pytest
from rest_framework.test import APIClient

from user.models import User

@pytest.fixture
def test_user(db):
    user = User.objects.create(name="Namezero", age=20)
    return user

@pytest.fixture
def api_client(test_user):
    client = APIClient()
    client.force_authenticate(user=test_user)
    return client 

@pytest.fixture
def user_1(db, test_user):
    user = User.objects.create(name="Nameone", age=21)
    return user

@pytest.fixture
def user_2(db, test_user):
    user = User.objects.create(name="Nametwo", age=22)
    return user