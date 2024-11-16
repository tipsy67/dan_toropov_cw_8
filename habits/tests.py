from logging import setLogRecordFactory

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Place, Reward, Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.test")
        self.place = Place.objects.create(name="test place")
        self.reward = Reward.objects.create(name="test reward")
        self.habit = Habit.objects.create(
            name="test habit",
            time_to_do="00:01:02",
            periodicity=1,
            time_to_complete=100,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)
        self.etalon_data = {
                "id": self.habit.pk,
                "place": None,
                "reward": None,
                "name": "test habit",
                "time_to_do": "00:01:02",
                "action": "",
                "is_nice_habit": False,
                "is_published": False,
                "periodicity": 1,
                "time_to_complete": 100,
                "start_time": None,
                "owner": self.user.pk,
                "linked_habit": None,
            }

    def test_habit_list(self):
        url = reverse("habits:my-habits")
        response = self.client.get(url)
        data = response.json().get("results")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, [self.etalon_data])


    def test_habit_retrieve(self):
        url = reverse("habits:my-habits-edit", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, self.etalon_data)

    def test_habit_update(self):
        url = reverse("habits:my-habits-edit", args=(self.habit.pk,))
        patch_data = {"action":"do_test"}
        response = self.client.patch(url, patch_data)
        data = response.json().get("action")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, patch_data)