from django.urls import reverse
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from rest_framework import status
from rest_framework.exceptions import ValidationError
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

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, self.etalon_data)

    def test_habit_update_delete(self):
        url = reverse("habits:my-habits-edit", args=(self.habit.pk,))
        patch_data = {"action": "do_test"}
        response = self.client.patch(url, patch_data)
        data = response.json().get("action")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, "do_test")
        self.assertEqual(IntervalSchedule.objects.all().count(), 1)
        self.assertEqual(PeriodicTask.objects.all().count(), 1)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
        self.assertEqual(PeriodicTask.objects.all().count(), 0)

    def test_habit_create(self):
        url = reverse("habits:my-habits-create")
        post_data = {
            "name": "test habit 2",
            "time_to_do": "02:03:04",
            "action": "test action",
            "periodicity": 1,
            "time_to_complete": 100,
        }
        response = self.client.post(url, post_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(IntervalSchedule.objects.all().count(), 1)
        self.assertEqual(PeriodicTask.objects.all().count(), 1)

    def test_habit_validate(self):
        url = reverse("habits:my-habits-create")
        post_data = {
            "name": "test habit 2",
            "time_to_do": "02:03:04",
            "action": "test action",
            "periodicity": 1,
            "time_to_complete": 100,
            "is_nice_habit": True,
        }
        response = self.client.post(url, post_data)
        new_habit_pk = response.json().get("id")

        url = reverse("habits:my-habits-edit", args=(self.habit.pk,))

        patch_data = {"periodicity": 99999}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

        patch_data = {"linked_habit": self.habit.pk}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

        patch_data = {"linked_habit": new_habit_pk}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        patch_data = {"is_nice_habit": True}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        patch_data = {"linked_habit": self.habit.pk}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

        patch_data = {"reward": self.reward.pk}
        response = self.client.patch(url, patch_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)
