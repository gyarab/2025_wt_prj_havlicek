from django.test import TestCase

from .models import Race, Result, Runner


class RunnerApiTests(TestCase):
    def setUp(self):
        self.runner = Runner.objects.create(
            first_name="Anna",
            last_name="Kovářová",
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
        self.assertEqual(response.json()["last_name"], "Kovářová")

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
                "last_name": "Nováková",
                "birth_date": "2009-11-05",
                "club": "AC Pardubice",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.runner.refresh_from_db()
        self.assertEqual(self.runner.last_name, "Nováková")


class RaceApiTests(TestCase):
    def setUp(self):
        self.race = Race.objects.create(
            name="Testovací běh",
            date="2026-06-20",
            location="Praha",
            distance_m=5000,
        )

    def test_list_races(self):
        response = self.client.get("/api/race")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["name"], "Testovací běh")

    def test_get_race_detail(self):
        response = self.client.get(f"/api/race/{self.race.id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["location"], "Praha")

    def test_create_race(self):
        response = self.client.post(
            "/api/race",
            {
                "name": "Večerní běh",
                "date": "2026-07-12",
                "location": "Brno",
                "distance_m": 10000,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Race.objects.filter(name="Večerní běh").exists())

    def test_update_race(self):
        response = self.client.put(
            f"/api/race/{self.race.id}",
            {
                "name": "Testovací běh",
                "date": "2026-06-20",
                "location": "Plzeň",
                "distance_m": 5000,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.race.refresh_from_db()
        self.assertEqual(self.race.location, "Plzeň")


class ResultApiTests(TestCase):
    def setUp(self):
        self.runner = Runner.objects.create(first_name="Eva", last_name="Dlouhá")
        self.race = Race.objects.create(
            name="Testovací běh",
            date="2026-06-20",
            location="Praha",
            distance_m=5000,
        )
        self.result = Result.objects.create(
            runner=self.runner,
            race=self.race,
            time_seconds=1234.5,
            position=1,
        )

    def test_list_results(self):
        response = self.client.get("/api/result")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["runner_id"], self.runner.id)

    def test_get_result_detail(self):
        response = self.client.get(f"/api/result/{self.result.id}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["race_id"], self.race.id)

    def test_result_formats_seconds_as_time(self):
        self.assertEqual(self.result.formatted_time, "00:20:34")

    def test_create_result(self):
        response = self.client.post(
            "/api/result",
            {
                "runner_id": self.runner.id,
                "race_id": self.race.id,
                "time_seconds": 1300.0,
                "position": 2,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Result.objects.filter(time_seconds=1300.0).exists())

    def test_update_result(self):
        response = self.client.put(
            f"/api/result/{self.result.id}",
            {
                "runner_id": self.runner.id,
                "race_id": self.race.id,
                "time_seconds": 1200.0,
                "position": 1,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.result.refresh_from_db()
        self.assertEqual(self.result.time_seconds, 1200.0)


class PublicFormTests(TestCase):
    def setUp(self):
        self.runner = Runner.objects.create(first_name="Eva", last_name="Dlouhá")

    def test_create_race_without_login(self):
        response = self.client.post(
            "/races/",
            {
                "name": "Městský běh",
                "date": "2026-06-20",
                "location": "Praha",
                "distance_m": 5000,
            },
        )

        self.assertRedirects(response, "/races/")
        self.assertTrue(Race.objects.filter(name="Městský běh").exists())

    def test_create_runner_without_login(self):
        response = self.client.post(
            "/runners/",
            {
                "first_name": "Petr",
                "last_name": "Rychlý",
                "birth_date": "2008-04-12",
                "club": "SK Brno",
            },
        )

        self.assertRedirects(response, "/runners/")
        self.assertTrue(Runner.objects.filter(last_name="Rychlý").exists())

    def test_create_result_without_login(self):
        race = Race.objects.create(
            name="Testovací běh",
            date="2026-06-20",
            location="Praha",
            distance_m=5000,
        )

        response = self.client.post(
            "/results/",
            {
                "runner": self.runner.id,
                "race": race.id,
                "time_seconds": 1234.5,
                "position": 1,
            },
        )

        self.assertRedirects(response, "/results/")
        self.assertTrue(Result.objects.filter(runner=self.runner, race=race).exists())
