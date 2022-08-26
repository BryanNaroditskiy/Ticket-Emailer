from distutils.util import subst_vars
from re import sub
from PIL import Image, ImageTk
from unicodedata import name
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class TicketMaker():
    
    def MakeTicket(ticketNum, digits, kindOfTicket): 
    
        #Opens the base ticket image and stores it in a object
        if(kindOfTicket=='PSU'):
            img = Image.open(r'Base Tickets\Student Ticket.png') 
        elif(kindOfTicket=='Non_PSU'):
            img = Image.open(r'Base Tickets\Non-Student Ticket.png')


        #Creates Object that allows the manipulation of image
        modImage = ImageDraw.Draw(img)


        #Sets font and size of text
        nameFont = ImageFont.truetype('fonts\CLEARSANS-REGULAR.TTF',50)


        #If statements that check how many digits are in the number of the ticket in order to be able change each indivual ticket number on the ticket image
        if(digits==1):
            #Creates and places text onto the ticket based off coordinates
            modImage.text((1492,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1557,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1622,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1687,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1753,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1818,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1883,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1949,450), str(ticketNum[0]), anchor="ms", font=nameFont, fill=(0,0,0))  #Converts the first digit of the number to string

        elif(digits==2):
            modImage.text((1492,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1557,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1622,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1687,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1753,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1818,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1883,450), str(ticketNum[0]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the first digit of the number to string
            modImage.text((1949,450), str(ticketNum[1]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the second digit of the number to string
        elif(digits==3):
            modImage.text((1492,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1557,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1622,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1687,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1753,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1818,450), str(ticketNum[0]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the first digit of the number to string
            modImage.text((1883,450), str(ticketNum[1]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the second digit of the number to string
            modImage.text((1949,450), str(ticketNum[2]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the third digit of the number to string
        elif(digits==4):
            modImage.text((1492,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1557,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1622,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1687,450), '0', anchor="ms", font=nameFont, fill=(0,0,0))
            modImage.text((1753,450), str(ticketNum[0]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the first digit of the number to string
            modImage.text((1818,450), str(ticketNum[1]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the second digit of the number to string
            modImage.text((1883,450), str(ticketNum[2]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the third digit of the number to string
            modImage.text((1949,450), str(ticketNum[3]), anchor="ms", font=nameFont, fill=(0,0,0)) #Converts the fourth digit of the number to string

        #Makes custom path for the image to be saved to
        ticketImgPath= 'Created Tickets/'+'DancePartyTicket_'+ticketNum+'.png'    

        #Saves image based off path                  
        img.save(ticketImgPath,quality=95)
        

        #img.show() #Shows ticket picture

        return ticketImgPath #Returns path of the image just saved









