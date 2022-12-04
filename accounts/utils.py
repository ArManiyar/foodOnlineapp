# helper function to run features
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage, message

from django.conf import settings

def detect_user(user):
    if user.role == 1:
        redirectUrl  = 'vendorDashboard'
        return redirectUrl
    elif user.role == 2:
        redirectUrl  = 'custDashboard'
        return redirectUrl
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
        return redirectUrl
    
'''def send_verification_email(request, user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    mail_subject = 'Please click below link to activate your account'
    message = render_to_string('accounts/emails/account_verfication_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # encodes the user primary id
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()'''

'''def send_pasword_reset_link(request, user):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    mail_subject = 'Reset you password'
    message = render_to_string('accounts/emails/reset_password_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # encodes the user primary id
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.send()
   ''' 
    # optimise the both abovr code
def send_reset_link(request, user, mail_subject, mail_template):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    subject = mail_subject
    message = render_to_string(mail_template, {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  # encodes the user primary id
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    mail = EmailMessage(subject, message, from_email, to=[to_email])
    mail.send()

def send_notification(mail_subject, mail_template, context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(mail_template, context)
    to_email = context['user'].email
    mail = EmailMessage(mail_subject,message,from_email, to=[to_email])
    mail.send()