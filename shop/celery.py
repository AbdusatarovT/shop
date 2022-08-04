
import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings') # путь к настройкам
django.setup()
app = Celery('shop') # название приложения
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) # для поисков задач

app.conf.beat_schedule = {
    'send_spam_from_john': {
        'task': 'applications.account.tasks.spam_email',
        'schedule': crontab(minute='*/1')
    }
}








#celery -A shop worker -l debug  ----- для запуска celery


# sudo apt install redis -- установка редис
# redis-server - запуск сервера
# sudo service redis-server stop --для остановки сервера
# sudo service redis-server start -- для запуска сервера

# pip install celery -- для установки селеру
# pip install celery[redis] -- для устанвки се4леру рддис библиотека для работы с редис
# celery -A shop beat --для запуска спама
# Настройка для редиса
# BROKER_URL = 'redis://127.0.0.1:6379/0'
# BROKER_TRANSPORT = 'redis'