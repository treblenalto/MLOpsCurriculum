# CRUD REST API - Django

## Database

### User

| Name     | Type | Nullable |
| :------- | :--- | :------: |
| id(PK)   | int  |          |
| name(UK) | str  |          |
| age      | int  |    O     |

## API

### 1. Get all users

#### URI

```
GET /user
```

#### Response

```
List[
    TypedDict{
        ”id”: int,
        “name”:str,
        “age”: int
    }
]
```

### 2. Get a user

#### URI

```
GET /user/<id:int>
```

#### Parameter

| Name | Type | Description |
| :--- | :--- | :---------- |
| id   | int  | user id     |

#### Response

```
TypedDict{
    ”id”: int,
    “name”:str,
    “age”: int
}
```

### 3. Create a user

#### URI

```
POST /user
```

#### Parameter

| Name | Type | Description |
| :--- | :--- | :---------- |
| name | str  | user name   |
| age  | int  | user age    |

#### Response

| Name    | Type | Description           |
| :------ | :--- | :-------------------- |
| success | bool | success indicator     |
| message | str  | success/error message |

#### Status Code

| Code | Description |
| :--: | :---------- |
| 201  | Created     |
| 400  | Bad Request |

### 4. Update a user

#### URI

```
PUT /user/<id:int>
```

#### Parameter

| Name | Type | Description |
| :--- | :--- | :---------- |
| name | str  | user name   |
| age  | int  | user age    |

#### Response

| Name    | Type | Description           |
| :------ | :--- | :-------------------- |
| success | bool | success indicator     |
| message | str  | success/error message |

#### Status Code

| Code | Description |
| :--: | :---------- |
| 200  | OK          |
| 400  | Bad Request |

### 5. Delete a user

#### URI

```
DELETE /user/<id:int>
```

#### Parameter

| Name | Type | Description |
| :--- | :--- | :---------- |
| id   | int  | user id     |

#### Response

| Name    | Type | Description           |
| :------ | :--- | :-------------------- |
| success | bool | success indicator     |
| message | str  | success/error message |

#### Status Code

| Code | Description |
| :--: | :---------- |
| 200  | OK          |
