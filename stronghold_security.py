import threading
from emailpassword import email_password, email_sender
from camera_capture import CameraCapture
from window_monitoring import WindowMonitoring
from remote_control import email_listener

def thread1():
    email_listener(email_sender, email_password)
def thread2():
    WindowMonitoring()

class StrongholdSecurity:
    def __init__(self) -> None:
        t1 = threading.Thread(target=thread1)
        t2 = threading.Thread(target=thread2)
        
        try: 
            CameraCapture()
        except: pass
        # Start the threads
        t1.start()
        t2.start()
                
