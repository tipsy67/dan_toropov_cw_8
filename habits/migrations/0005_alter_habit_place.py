# Generated by Django 5.1.2 on 2024-11-09 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0004_alter_habit_reward"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="place",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="habits",
                to="habits.place",
                verbose_name="место",
            ),
        ),
    ]
