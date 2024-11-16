from django.db import models

NULLABLE = {"blank": True, "null": True}


class Place(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(**NULLABLE, verbose_name="описание")

    def __str__(self):
        return f"Place:{self.name}"

    class Meta:
        verbose_name = "место"
        verbose_name_plural = "места"


class Reward(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(**NULLABLE, verbose_name="описание")

    def __str__(self):
        return f"Reward:{self.name}"

    class Meta:
        verbose_name = "вознаграждение"
        verbose_name_plural = "вознаграждения"


class Habit(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    owner = models.ForeignKey(
        to="users.User",
        on_delete=models.CASCADE,
        **NULLABLE,
        related_name="habits",
        verbose_name="владелец",
    )
    place = models.ForeignKey(
        to="Place",
        on_delete=models.PROTECT,
        **NULLABLE,
        related_name="habits",
        verbose_name="место",
    )
    time_to_do = models.TimeField(verbose_name="время")
    action = models.CharField(max_length=200, verbose_name="действие")
    is_nice_habit = models.BooleanField(default=False, verbose_name="приятность")
    is_published = models.BooleanField(default=False, verbose_name="публичность")
    linked_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="связанная привычка"
    )
    reward = models.ForeignKey(
        to="Reward",
        on_delete=models.PROTECT,
        **NULLABLE,
        related_name="habits",
        verbose_name="вознаграждение",
    )
    periodicity = models.PositiveIntegerField(verbose_name="периодичность")
    time_to_complete = models.PositiveIntegerField(verbose_name="время на выполнение")
    start_time = models.DateTimeField(**NULLABLE, verbose_name="первое напоминание")

    def __str__(self):
        return f"Habit:{self.name}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"

