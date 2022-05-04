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
    assert data[1]["id"] == user_1.id, "id is not correct"
    assert data[2]["id"] == user_2.id, "id is not correct"


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


# create a user
@pytest.mark.parametrize(
    "request_data, expected_status_code",
    [
        # post a user
        pytest.param(
            {"name": "Namethree", "age": 23},
            status.HTTP_201_CREATED,
            id="post: valid request",
        ),
        # post a user with no age - nullable
        pytest.param(
            {"name": "Noage"},
            status.HTTP_201_CREATED,
            id="post: valid request with no age",
        ),
        # post a user with negative age
        pytest.param(
            {"name": "Negativeage", "age": -1},
            status.HTTP_400_BAD_REQUEST,
            id="post: invalid request with negative age",
        ),
        # post a user with no name
        pytest.param(
            {"age": 23},
            status.HTTP_400_BAD_REQUEST,
            id="post: invalid request with no name",
        ),
    ],
)
def test_post(api_client, request_data, expected_status_code):
    response = api_client.post(
        reverse_lazy("user-list"), data=request_data, format="json"
    )
    assert response.status_code == expected_status_code, "status code is not correct"
    if status.is_success(response.status_code):
        response_data = response.data
        for key, values in request_data.items():
            assert response_data[key] == values, f"{key} is not correct"


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
