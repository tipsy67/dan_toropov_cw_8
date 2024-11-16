from django.contrib.auth.models import AbstractUser
from django.db import models

from habits.models import NULLABLE


class User(AbstractUser):
    tg_chat_id = models.CharField(
        max_length=50, **NULLABLE, verbose_name="телеграм chat id"
    )

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
