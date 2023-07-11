from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from emailpassword import email_sender, email_password
import cv2
import smtplib
import socket
import requests

class CameraCapture:
    """Captures 3 pictures of the person that is using the pc"""
    def __init__(self) -> None:
        for x in range(3):
            cap = cv2.VideoCapture(0)

            ret, frame = cap.read()

            cv2.imwrite(f'intruder{x}.jpg', frame)

            cap.release()
        self.send_email(email_sender, 
                        email_password, 
                        "projektykandl@gmail.com", 
                        "Suspicious activity on your device", 
                        f"Name: {socket.gethostname()}, IP Address: {self.get_public_ip()}", 
                        ["intruder0.jpg", "intruder1.jpg", "intruder2.jpg"])
        


    def send_email(self, sender_email, sender_password, recipient_email, subject, message, image_paths):
        # Create a multipart message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message as plain text
        msg.attach(MIMEText(message, 'plain'))

        # Attach the images
        for image_path in image_paths:
            with open(image_path, 'rb') as f:
                img_data = f.read()
            image = MIMEImage(img_data, name='intruder.jpg')  # Modify the name as per your requirement
            msg.attach(image)

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)

        # Clean up
        server.quit()
    
    def get_public_ip(self):
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            data = response.json()
            public_ip = data['ip']
            return public_ip
        else:
            return None

CameraCapture()