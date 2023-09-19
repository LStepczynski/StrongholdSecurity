# StrongholdSecurity
This Repository contains a program that monitors the actions of a person using the PC if they do not input the password. It allows for remote commands to the device and updates the owner of any action done on the device as well as the overall location of the device.
For the program to function poperly a file with gmail adress with password will need to be exported to certain files. 

# How to use
Clone the repository to a folder, than create a **emailpassword.py** file in which create 3 variables <br>
- email_password
- email_sender
- email_reciever
  
Inside of them put the **Password to your email, Address to your email and Address to the email that you want the security notfications to be sent to**. Than create a shortcut to the main.py and put it in the autostart so the application is run each time the computer is launched.

### Remote Control
To remotly control your own computer the program has to be active on your computer. Use commands by sending an email with a command in the subject field to your email adress that you added in **email_password** variable. The commands are the following:
- -MESSAGE-:**text** | replace **text** with message that you want to remotly display on your computer
- -HISTORY- | Send the window history of you computer to the email address provided in the **email_reciever** variable
- -SHUTDOWN- | Shuts down the computer

