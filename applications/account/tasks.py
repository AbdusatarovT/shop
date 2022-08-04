import time
from django.core.mail import send_mail

from applications.spam.models import Contact
from shop.celery import app


@app.task
def celery_send_confirmation_email(code, email):
    time.sleep(10) # время для выполнния в онновом режиме
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'From shop project', # заголовок сообщения
        full_link, # текст сообщения
        'lgtahir93@gmail.com', # от кого
        [email] # кому
    )

@app.task
def celery_send_order_email(text, email):
    time.sleep(10)
    send_mail(
        'Подтверждения заказа!',
        f'Ваш заказ: {text}',
        'lgtahir93@gmail.com',
        [email]
    )

@app.task
def spam_email():
    for i in Contact.objects.all():
        full_link = f'Hello'
        send_mail(
            'From shop project',
            full_link,
            'lgtahir93@gmail.com',
            [i.email]
        )

