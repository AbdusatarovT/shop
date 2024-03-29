from django.core.mail import send_mail



def send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/api/v1/account/active/{code}'
    send_mail(
        'From shop project', # заголовок сообщения
        full_link, # текст сообщения
        'lgtahir93@gmail.com', # от кого
        [email] # кому
    )




def forgot_password_email(code, email):
    send_mail(
        'Восстановление пароля',
        f'Ваш код подтверждения: {code}',
        'lgtahir93@gmail.com',
        [email]
    )

def send_order_email(text, email):
    send_mail(
        'Подтверждения заказа!',
        f'Ваш заказ: {text}',
        'lgtahir93@gmail.com',
        [email]
    )
