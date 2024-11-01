from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
