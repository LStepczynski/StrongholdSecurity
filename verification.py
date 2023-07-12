import tkinter as tk
from tkinter import messagebox
from datetime import date
from stronghold_security import StrongholdSecurity

class VerificationWindow():
    """ A pop up Window that verifies the user """
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title('Verification Window')
        self.window.geometry('300x200')
        self.window.columnconfigure(0, weight=1)
        self.window.configure(bg="black")
        self.window.protocol("WM_DELETE_WINDOW", self.popup) # Disable the option to close the window

        self.password_var = tk.StringVar()
        self.password_input = tk.Entry(self.window, width=6, font=('', 30), textvariable=self.password_var)
        self.password_input.grid(row=1, pady=50)

        self.submit_button = tk.Button(text='Submit', command=self.check_password)
        self.submit_button.grid()

        self.window.after(60000, self.time_up) # Close the window after 1 minute

        self.window.mainloop()

    def check_password(self):
        if self.password_var.get() == date.today().strftime('%Y-%m-%d'):
            self.window.destroy()

    def time_up(self): # After 1 minute activate the monitoring program
        StrongholdSecurity()
        self.window.destroy()
    
    def popup(self):
        # Create the root window
        window = tk.Tk()
        window.withdraw()  # Hide the root window

        # Show the popup message box
        messagebox.showinfo("Popup Message", "Please input the password or wait for the window to disssapear")

        # Destroy the root window
        window.destroy()


