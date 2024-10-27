from django.db import models

NULLABLE ={"blank":True, "null":True}

class Place(models.Model):
    name = models.CharField(max_length=100, verbose_name='')
    description = models.TextField(**NULLABLE, verbose_name='')

class Reward(models.Model):
    name = models.CharField(max_length=100, verbose_name='')
    description = models.TextField(**NULLABLE, verbose_name='')

class Habit(models.Model):
    owner = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="habits", verbose_name='')
    place = models.ForeignKey(to="Place",on_delete=models.PROTECT, related_name="habits", verbose_name='')
    time_to_do = models.TimeField(verbose_name='')
    action = models.CharField(max_length=200, verbose_name='')
    is_nice_habit = models.BooleanField(default=False, verbose_name='')
    is_published = models.BooleanField(default=False, verbose_name='')
    linked_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name='')
    reward = models.ForeignKey(to="Reward",on_delete=models.PROTECT, related_name="habits", verbose_name='')
    periodicity = models.PositiveIntegerField(verbose_name='')
    time_to_complete = models.TimeField(verbose_name='')


