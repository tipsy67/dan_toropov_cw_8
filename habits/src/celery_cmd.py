import json
from datetime import date, datetime

from django_celery_beat.models import IntervalSchedule, PeriodicTask

from habits.models import Habit


def start_task(obj: Habit):
    name_task = f"Habit_{obj.pk}"
    start_time = datetime.combine(datetime.now().date(), obj.time_to_do)

    interval = IntervalSchedule.objects.filter(
        every=obj.periodicity, period="minutes"
    ).first()
    if interval is None:
        interval = IntervalSchedule.objects.create(every=obj.periodicity, period="minutes")

    task = PeriodicTask.objects.filter(name=name_task).first()
    if task is None:
        PeriodicTask.objects.create(
            name=name_task,
            task="habits.tasks.send_reminder",
            args=json.dumps([obj.pk]),
            interval=interval,
            start_time=start_time,
        )
    else:
        task.interval = interval
        task.start_time = start_time
        task.save()


def delete_task(obj: Habit):
    name_task = f"Habit_{obj.pk}"
    task = PeriodicTask.objects.filter(name=name_task).first()
    if task is not None:
        task.delete()
