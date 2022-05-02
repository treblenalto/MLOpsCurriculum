# Locust Performance Test

> EC2 endpoint: http://13.124.253.28:8000 <br>
> ECS endpoint: http://3.35.197.217:8000

Start performance test with Locust

```
locust -f locustfile.py
```

## EC2

### Read

![ec2-read](https://user-images.githubusercontent.com/63901494/166228646-42f17f8c-477c-4910-80bf-157c81377b1e.png)

- POST 에 대한 테스트를 진행 후 Read 만 따로 진행하여 DB에 읽어올 데이터가 많이 쌓였던 상태
- 사용자가 52명 시점으로부터 트래픽 과부하로 인해 서버 에러가 남.. 터짐
- 사용자 50명 정도 기준 단위 시간당 최대 1.5개 처리

### Write

![ec2-write](https://user-images.githubusercontent.com/63901494/166228146-b3996627-94ef-482b-a81c-8c15aa283309.png)

- 동시접속자 50명 기준 평균적으로 590ms 의 response time을 보임
- 단위시간당 최대 82개의 처리량
- failure 는 일어나지 않음

## ECS

### Read

![ecs-read-charts](https://user-images.githubusercontent.com/63901494/166222671-165ce062-7722-4435-a675-eaa2b44e4e31.png)

- POST에 대한 테스트를 이미 한 번 진행 후 Read 만 따로 본 것이라 DB에 읽어올 데이터가 많이 쌓였던 상태
- EC2에서처럼 서버가 터지지는 않지만 DB에 read 작업이 쌓여 response time 이 증가하는 부분들을 볼 수 있음
- 동시접속자 100명 기준 평균적으로 24000ms 의 response time을 보임
- 단위시간당 최대 7개의 처리량

### Write

![ecs-write](https://user-images.githubusercontent.com/63901494/166225137-b9726334-1528-447b-a290-d51d02af5ede.png)

- 동시접속자 50명 기준 평균적으로 1800ms의 response time 을 보임
- 단위시갖당 최대 28개의 처리량
- failure 는 일어나지 않음

## Analysis

- 전반적으로 ECS 보다 EC2가 Response Time 이 훨씬 적음. EC2와 ECS의 하드웨어적인 차이 때문
  - EC2 t2.micro 인스턴스: 1vCPU, 1GB Memory
  - ECS Fargate: 0.25vCPU, 512MB Memory
- 중간에 서버가 터지는 EC2보다 ECS가 더 안정적
