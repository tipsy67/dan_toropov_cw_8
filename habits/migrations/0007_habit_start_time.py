# Generated by Django 5.1.2 on 2024-11-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0006_alter_habit_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="habit",
            name="start_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="первое напоминание"
            ),
        ),
    ]
