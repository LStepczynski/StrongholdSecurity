import cv2
from email.message import EmailMessage
import ssl
import smtplib
import time

class CameraCapture:
    """Captures 3 pictures of the person that is using the pc"""
    def __init__(self) -> None:
        for x in range(3):
            cap = cv2.VideoCapture(0)

            ret, frame = cap.read()

            cv2.imwrite(f'intruder{x}.jpg', frame)

            cap.release()


    def send_email(email_sender, email_password, email_recevier, subject, body):
        """Sends an email"""
        em = EmailMessage()
        em['from'] = email_sender
        em['to'] = email_recevier
        em['subject'] = subject
        em.set_content(body)

        context1 = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context1) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_recevier, em.as_string())