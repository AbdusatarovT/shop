from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# TODO: рефлизовать отправку спам сообщений всем обьуктам из Contact.
# 2 При создании товара отпровлять сообщнние всем обьектам из модельки Контакт
# Развернуть проект с Селеру