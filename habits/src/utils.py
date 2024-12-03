import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText

import requests

from config.settings import TG_TOKEN
from habits.models import Habit


def send_telegram_message(obj: Habit):
    """Функция отправки телеграм напоминания о привычке"""
    text_good_dog = None

    linked_habit = obj.linked_habit
    if linked_habit:
        text_good_dog = linked_habit.action

    reward = obj.reward
    if reward:
        text_good_dog = reward.description

    if text_good_dog is not None:
        text_good_dog = "После выполнения не забудьте про: " + text_good_dog

    payload = {
        "chat_id": obj.owner.tg_chat_id,
        "text": f"Запланированная привычка: {obj.name}\n"
        + f"Вы должны сделать: {obj.action}\n"
        + f"Время на выполнение: {obj.time_to_complete} сек.\n"
        + f"{text_good_dog}",
    }

    requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", data=payload)


def sendmail(recipients_emails: list, title: str, content: str):
    """
    Функция отправки писем
    """
    smtp_server = "smtp.yandex.ru"

    login = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASSWORD")

    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = Header(title, "utf-8")
    msg["From"] = login
    msg["To"] = ", ".join(recipients_emails)

    s = smtplib.SMTP(smtp_server, 587, timeout=10)
    s.set_debuglevel(1)
    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg["From"], recipients_emails, msg.as_string())
    finally:
        # print(msg)
        s.quit()
