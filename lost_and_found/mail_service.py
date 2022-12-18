from django.core.mail import send_mail
from django.conf import settings


def send_forget_password_mail(email, token):
    try:
        subject = 'Your forgot password link'
        message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change-password/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        # print('mail sent')
        return True
    except Exception as e:
        print(e)
        return False


def send_point_purchase_mail(name):
    try:
        subject = 'Point Purchase Request'
        message = f'{name} requested for purchase some points. Click the link given below to view.\n\n http://127.0.0.1:8000/admin-login'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['lostandfound72428@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        return True
    except Exception as e:
        print(e)
        return False


def send_point_success_mail(email):
    try:
        subject = 'Point Added'
        message = f'Your requested point has been added to your account. Click the link given below to view.\n\n http://127.0.0.1:8000'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return True

    except Exception as e:
        print(e)
        return False


def send_claim_rejection_mail(email):
    try:
        subject = 'Smart Lost and Found - Claim Rejected'
        message = f'Your request for claiming the item has been rejected by the admin. Click the link given below to view.\n\n http://127.0.0.1:8000'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        return True

    except Exception as e:
        print(e)
        return False


def send_claim_acception_mail(user, email):
    try:
        subject = 'Smart Lost and Found - Item found'
        message = f'''Your item has been found.

        The details of the person who found your item is:
                        Name: {user[1]}
                        Email: {user[2]}
                        Phone: {user[4]}
                        Hostel: {user[5]}
        
        Please contact the person for further details.  
        If person is unavailable, please contact the admin'''

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        print(message)
        send_mail(subject, message, email_from, recipient_list)
        return True

    except Exception as e:
        print(e)
        return False
