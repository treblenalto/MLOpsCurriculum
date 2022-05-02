from locust import HttpUser, task
import random
import string

class PerformanceTest(HttpUser):
    @task
    def get_all_users(self):
        self.client.get("/users/")

    @task
    def create_users(self):
        self.client.post(
            "/users/",
            json={
                "name": "robot"
                + "".join(random.choice(string.ascii_uppercase) for i in range(5)),
                "age": 20,
            },
        )
