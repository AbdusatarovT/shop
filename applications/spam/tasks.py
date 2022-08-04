from django.core.mail import send_mail

from applications.spam.models import Contact
from shop.celery import app


@app.task
def spam_email2(body):
    for i in Contact.objects.all():
        full_link = f'Привет на нашем сайте появился новый товар {body}'
        send_mail(
            'From shop project',
            full_link,
            'lgtahir93@gmail.com',
            [i.email]
        )