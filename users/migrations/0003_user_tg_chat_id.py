# Generated by Django 5.1.2 on 2024-11-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="телеграм chat id"
            ),
        ),
    ]
