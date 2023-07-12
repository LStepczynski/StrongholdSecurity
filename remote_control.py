from camera_capture import CameraCapture
from window_monitoring import WindowMonitoring
from emailpassword import email_password, email_sender
import tkinter as tk
from tkinter import messagebox
import imaplib
import email
import time
import os

def show_popup(message):
    # Create the root window
    root = tk.Tk()

    # Show the popup message box
    root.withdraw()
    messagebox.showinfo("Popup Message", message)
    

    # Destroy the root window and exit the program
    root.destroy()

def email_listener(username, password):
    while True:
        # Connect to the Gmail IMAP server
        mail = imaplib.IMAP4_SSL('imap.gmail.com')

        try:
            # Log in to the Gmail account
            mail.login(username, password)

            # Select the mailbox (in this case, the inbox)
            mail.select('inbox')

            # Search for new unread emails
            status, data = mail.search(None, 'UNSEEN')

            if status == 'OK':
                email_ids = data[0].split()

                for email_id in email_ids:
                    status, data = mail.fetch(email_id, '(RFC822)')

                    if status == 'OK':
                        # Parse the email
                        raw_email = data[0][1]
                        msg = email.message_from_bytes(raw_email)
                        subject = msg['Subject']

                        if "-MESSAGE-:" in subject:
                            show_popup(subject)
                        elif "-PC SHUTDOWN-" == subject:
                            os.system("shutdown /s /t 0")
                        elif "-PICTURE-" == subject:
                            CameraCapture()
                        elif "-HISTORY-" == subject:
                            WindowMonitoring.send_email(WindowMonitoring, email_sender, 
                            email_password, 
                            "projektykandl@gmail.com",
                            f"Window History",
                            "An suspicious activity has been recorded on your device.",
                            "window_history.txt"
                            )

            # Sleep to wait before checking for new emails again
            time.sleep(10)

        except imaplib.IMAP4.abort as e:
            print(f"IMAP error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the connection
            try:
                mail.logout()
            except Exception as e:
                print(f"Error occurred while logging out: {e}")



