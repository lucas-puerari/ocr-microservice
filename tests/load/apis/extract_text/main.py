from locust import HttpUser, task, between


class User(HttpUser):
    """
    TODO
    """
    wait_time = between(1, 1.5)

    @task
    def extract_text_from_hello_world_sample(self):
        sample1 = open('../assets/images/ocr-hello-world-sample.png', 'rb')
        files = [
            ('sample1', sample1),
        ]

        with self.client.post(
            "/extract-text",
            files=files,
            catch_response=True
        ) as response:

            if response.status_code != 200:
                response.failure("Wrong statusCode")
