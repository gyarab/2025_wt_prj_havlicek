from django.test import TestCase

from .models import Runner


class RunnerApiTests(TestCase):
    def setUp(self):
        self.runner = Runner.objects.create(
            first_name="Anna",
            last_name="Kovarova",
            birth_date="2009-11-05",
            club="AC Pardubice",
        )

    def test_list_runners(self):
        response = self.client.get("/api/runner")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["first_name"], "Anna")

    def test_get_runner_detail(self):
        response = self.client.get(f"/api/runner/{self.runner.id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["last_name"], "Kovarova")

    def test_create_runner(self):
        response = self.client.post(
            "/api/runner",
            {
                "first_name": "Jan",
                "last_name": "Svoboda",
                "birth_date": "2006-02-17",
                "club": "Sparta Praha",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Runner.objects.filter(last_name="Svoboda").exists())

    def test_update_runner(self):
        response = self.client.put(
            f"/api/runner/{self.runner.id}",
            {
                "first_name": "Anna",
                "last_name": "Novakova",
                "birth_date": "2009-11-05",
                "club": "AC Pardubice",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.runner.refresh_from_db()
        self.assertEqual(self.runner.last_name, "Novakova")
