# Generated by Django 5.1.2 on 2024-11-16 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0007_habit_start_time"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="habit",
            options={
                "ordering": ("pk",),
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
            },
        ),
    ]
