from posixpath import abspath
import win32com.client as win32
import os
from pathlib import Path, WindowsPath

class Email:
    def SendAnEmail(emailAddress,imagePath):                                                                              # Method that takes the email address and the list storing the paths of the ticket images
    
        outlook = win32.Dispatch('outlook.application')                                                                   # Creating a COM Object based off Outlook
        mail = outlook.CreateItem(0)                                                                                      # Creates an email from that COM Object
        mail.To = emailAddress                                                                                            # Adds the To email to the email being sent
        mail.Subject = 'Confirmation of Purchase of Hillel Global Dance Party Ticket'                                     #Adds Subject Line to the email being sent
        mail.Body = 'Thank you for purchasing your Global Dance Party ticket! Please bring your ticket and ID to\
        show at the door. Have a great day! \n \n Reminder: No bags allowed at the event'                                 # Adds Body of text to the email being sent

        for x in imagePath:                                                                                               # Iterates through the imagePath list and pulls the values out of the list
            abs_path = os.path.abspath(x)                                                                                 # Finds the absolute path of the ticket picture
            mail.Attachments.Add(abs_path)                                                                                # To attach a file to the email

        mail.Send()                                                                                                       # Sends Email