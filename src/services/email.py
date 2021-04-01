import logging
import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from src.enums.email import EMAIL_CONFIRMATION_TEMPLATE

logger = logging.getLogger(__name__)


class EmailService:
    def __init__(self, sendgrid_api_key, sender):
        self.sendgrid_api_key = sendgrid_api_key
        self.sender = sender
        if not sender:
            raise Exception('Email service is not configured. EMAIL_ADDRESS needs to be added.')
        if not sendgrid_api_key:
            raise Exception('Email service is not configured. SENDGRID_API_KEY Address needs to be added.')

    def send_email(self, to, subject, content):
        message = Mail(
            from_email=self.sender,
            to_emails=to,
            subject=subject,
            html_content=content)
        try:
            sg = SendGridAPIClient(self.sendgrid_api_key)
            sg.send(message)
        except Exception as e:
            logger.error(f"We were unable to send an email to {to}")
            logger.error(e)

    def send_confirmation_email(self, user, token):
        url = f'{settings.SERVER_HOST}:{settings.SERVER_PORT}/email-confirmation?token={token}'
        email_content = EMAIL_CONFIRMATION_TEMPLATE.format(user.first_name, url)
        self.send_email(user.email, 'Welcome to Fii Practic App', email_content)
