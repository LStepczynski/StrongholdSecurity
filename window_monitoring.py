import pygetwindow as gw
from datetime import datetime
import time

class WindowMonitoring:
    """Monitors what browsers and tabs are open on the computer"""
    def __init__(self) -> None:
        self.last_windows = set()  # Initialize as an empty set
        while True:
            self.check_open_windows()
            time.sleep(5)

    def check_open_windows(self):
        windows = gw.getAllTitles()
        open_windows = set()
        for window in windows:
            if window.strip():  # Check if the title is non-empty after stripping whitespace
                open_windows.add(window)
        
        if open_windows != self.last_windows:
            with open('window_history.txt', 'a') as f:
                f.write(f'WINDOWS: {open_windows}, TIME: {datetime.now()} \n')
                self.last_windows = open_windows
        

WindowMonitoring()
