import logging
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


logger = logging.getLogger(__name__)


def send_email(to, subject, content):
    from_ = os.environ.get('EMAIL_ADDRESS')
    if not from_:
        raise Exception('Email service is not configured. EMAIL_ADDRESS needs to be added.')
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        raise Exception('Email service is not configured. SENDGRID_API_KEY Address needs to be added.')

    message = Mail(
        from_email=from_,
        to_emails=to,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(api_key)
        sg.send(message)
    except Exception as e:
        logger.error(f"We were unable to send an email to {to}")
        logger.error(e)


if __name__ == '__main__':
    send_email("test.com", "Title", "content")
