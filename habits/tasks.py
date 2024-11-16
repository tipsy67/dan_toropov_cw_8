from celery import shared_task

from habits.models import Habit
from habits.src.utils import send_telegram_message


@shared_task
def send_reminder(*args, **kwargs):
    obj = Habit.objects.filter(pk=args[0]).first()
    send_telegram_message(obj)
