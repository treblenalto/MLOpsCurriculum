## Transfer Money

### Description

특정 유저의 돈을 다른 유저에게 전달한다.

### URI

```
POST /transactions/send
```

### Parameter

|   Name   | Type |     Description     | Required |
| :------: | :--: | :-----------------: | :------: |
| sndr_id  | int  |  sender account id  |    O     |
| rcvr_id  | int  | receiver account id |    O     |
|  amount  | int  |  money being sent   |    O     |
| currency | str  |    currency code    |    O     |

### Response

|  Name   | Type |         Description         | Required |
| :-----: | :--: | :-------------------------: | :------: |
| success | bool | true=success, false=failure |    O     |
|  error  | str  |        error message        |          |
