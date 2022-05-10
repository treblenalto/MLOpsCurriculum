# MLOps Curriculum

I'm an engineer at Corca!

## API

Simple CRUD API handling user's name and age data made with django and postgresql<br>
[Documentation](https://github.com/Taehee-K/MLOpsCurriculum/tree/main/src)

- Get all users: `GET /users`
- Get a user: `GET /users/<id:int>`
- Create a user: `POST /users`
- Update a user: `PUT /users/<id:int>`
- Delete a user: `DELETE /users/<id:int>`

## Usage

### Installation

```
git clone https://github.com/Taehee-K/MLOpsCurriculum.git
cd MLOpsCurriculum
pip install -r requirements.txt     # when using pip
conda env create -f packagelist.yml # when using conda
```

### Local

```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Run using docker

```
docker compose up
```

### ECS

```
docker context create ecs mlopscurriculum
docker context use mlopscurriculum
docker compose --file docker-compose-ecs.yml up
```

## Testing

Unit test & End to end test

```
pytest
```

Performance test
```
cd performance
locust -f locustfile.py
```
[Report on EC2 and ECS Performance test](./assignments/performance.md)

---

## Phase1

> EC2 endpoint: http://13.124.253.28:8000 <br>
> ECS endpoint: http://3.35.23.6:8000

### Summary

<details>
<summary>RESTful한 API에 대해 공부 후 CRUD API를 개발, DB와 연결, Docker를 사용해 AWS EC2와 ECS로 배포한다.</summary>
<p>

| Course                  | :balloon:                                                |
| :---------------------- | :------------------------------------------------------- |
| MLOps란 무엇인가        |                                                          |
| Git                     | [#1](https://github.com/Taehee-K/MLOpsCurriculum/pull/1) |
| RESTful API             | [#2](https://github.com/Taehee-K/MLOpsCurriculum/pull/2) |
| Database                |                                                          |
| Server Development      | [#3](https://github.com/Taehee-K/MLOpsCurriculum/pull/3) |
| Docker                  | [#6](https://github.com/Taehee-K/MLOpsCurriculum/pull/6) |
| Cloud Computing Service | [#9](https://github.com/Taehee-K/MLOpsCurriculum/pull/9) |

</p>
</details>

### Review

- ML엔지니어로서 모델이 배포되는 과정에 대해 이해도를 키우고 싶어서 시작한 MLOps Curriculum이었는데 실제 서버 개발, 배포를 진행하며 소프트웨어 엔지니어로서의 시야가 넓어진 것 같다.
- API, Docker, EC2 & ECR 배포를 진행하면서 컴퓨터 네트워크의 이론들이 실제로 어떻게 적용되는지 공부하게 되었다.
- 사용가능한 스택이 자유로 되어있어 API를 만들 때 어떤 프레임워크를 사용할지 고민을 많이 했다. 최종적으로 django를 선택했는데 CRUD API 개발 시 대부분의 컴포넌트들이 추상화가 너무 잘 되어있어서 편했다.
- 도커파일을 만들 때 이전에는 그냥 docker hub에 있는 큰 이미지를 사용했다면 경량화 이미지 사용, 빌드/배포 속도를 고려하는 등 최적화 방법들에 대해 고민해 보게 되었다.
- 처음 해보는 것들이라 시간도 오래 걸렸고 에러도 많이 생겼는데 디버깅 실력이 는 것 같다.
- 가독성 높은 코드에 대한 고민이 계속 필요하다.

### Feedback

- MLOps 문외한으로서 커리큘럼 순서나 내용, 실습과정들이 잘 구성되어 있었다고 생각한다.
- 실습을 진행한 후 코드리뷰를 통해 피드백을 받는 과정에서 많이 도움을 받았고, 또 덕분에 성장할 수 있었다.
- 커리큘럼 중간중간에 참고자료들이 많았는데 (개인적으로) 영상은 잘 안 보게 되어서 영상보다는 블로그 및 공식문서들 위주로 공부했다.
