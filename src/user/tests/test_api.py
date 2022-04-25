import pytest
from django.urls import reverse_lazy
from rest_framework import status

# get all users
def test_get_user_list(api_client, test_user, user_1, user_2):
    response = api_client.get(reverse_lazy("user-list"))
    assert response.status_code == status.HTTP_200_OK, "status code is not correct"

    data = response.data
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["id"] == test_user.id, "id is not correct"
    assert data[0]["name"] == test_user.name, "name is not correct"
    assert data[0]["age"] == test_user.age, "age is not correct"
    assert data[1]["id"] == user_1.id, "id is not correct"
    assert data[1]["name"] == user_1.name, "name is not correct"
    assert data[1]["age"] == user_1.age, "age is not correct"
    assert data[2]["id"] == user_2.id, "id is not correct"
    assert data[2]["name"] == user_2.name, "name is not correct"
    assert data[2]["age"] == user_2.age, "age is not correct"


# get a user
def test_get_user_detail(api_client, test_user, user_1, user_2):
    response = api_client.get(reverse_lazy("user-detail", kwargs={"pk": test_user.id}))
    assert response.status_code == status.HTTP_200_OK, "status code is not correct"

    response_data = response.data
    assert isinstance(response_data, dict)
    for key, values in response_data.items():
        assert response_data[key] == values, f"{key} is not correct"


# get a user with invalid id
def test_get_user_detail_invalid_id(api_client):
    response = api_client.get(reverse_lazy("user-detail", kwargs={"pk": -1}))
    assert (
        response.status_code == status.HTTP_404_NOT_FOUND
    ), "status code is not correct"


# create(post) a user
def test_post_user(api_client):
    request_data = {"name": "Namethree", "age": 23}
    response = api_client.post(
        reverse_lazy("user-list"), data=request_data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED, "status code is not correct"

    response_data = response.data
    for key, values in request_data.items():
        assert response_data[key] == values, f"{key} is not correct"


# create a user with no age - age nullable
def test_post_user_no_age(api_client):
    request_data = {"name": "Noage"}
    response = api_client.post(
        reverse_lazy("user-list"), data=request_data, format="json"
    )
    assert response.status_code == status.HTTP_201_CREATED, "status code is not correct"
    response_data = response.data
    for key, values in response_data.items():
        assert response_data[key] == values, f"{key} is not correct"


# create a user with negative age
def test_post_user_negative_age(api_client):
    request_data = {"name": "Negativeage", "age": -1}
    response = api_client.post(
        reverse_lazy("user-list"), data=request_data, format="json"
    )
    assert (
        response.status_code == status.HTTP_400_BAD_REQUEST
    ), "status code is not correct"
    response_data = response.data
    assert isinstance(response_data, dict)


# create a user with no name
def test_post_user_no_name(api_client):
    request_data = {"age": 23}
    response = api_client.post(
        reverse_lazy("user-list"), data=request_data, format="json"
    )
    assert (
        response.status_code == status.HTTP_400_BAD_REQUEST
    ), "status code is not correct"
    response_data = response.data
    assert isinstance(response_data, dict)


# update a user
def test_update_user(api_client, test_user):
    request_data = {"name": "UpdatedName", "age": 20}
    response = api_client.put(
        reverse_lazy("user-detail", kwargs={"pk": test_user.id}),
        data=request_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK, "status code is not correct"

    response_data = response.data
    for key, values in request_data.items():
        assert response_data[key] == values, f"{key} is not correct"


# update a user with invalid id
def test_update_user_invalid_id(api_client):
    request_data = {"name": "UpdatedName", "age": 20}
    response = api_client.put(
        reverse_lazy("user-detail", kwargs={"pk": -1}), data=request_data, format="json"
    )
    assert (
        response.status_code == status.HTTP_404_NOT_FOUND
    ), "status code is not correct"


# delete a user
def test_delete_user(api_client, test_user):
    response = api_client.delete(
        reverse_lazy("user-detail", kwargs={"pk": test_user.id})
    )
    assert response.status_code == status.HTTP_200_OK, "status code is not correct"
    response_data = response.data
    for key, values in response.data.items():
        assert response_data[key] == values, f"{key} is not correct"


# delete a user with invalid id
def test_delete_user_invalid_id(api_client):
    with pytest.raises(Exception):
        raise api_client.delete(reverse_lazy("user-detail", kwargs={"pk": -1}))
