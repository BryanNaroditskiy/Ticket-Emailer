from tempfile import tempdir
import pandas as pd
import TicketMakerClass as tm
import EmailMembers as em


def ReadExcelAndMakeEmail():
    spreadSheet = pd.read_excel('Excel Files\Ticket Sales-Global Dance Party.xlsx')  # Opens and reads the excel file
    #print(spreadSheet)                                                              # To make
    
    x=0
    ticketImagePath = []                                                             #List that will hold path to created tickets

    while(x<len(spreadSheet.index)):                                                 # Loops as many times as there are rows in the document
        ticketImagePath.clear()
        if(spreadSheet['# of PSU Tickets'][x] > 0):
            numberOf_PSU_Tickets = spreadSheet['# of PSU Tickets'][x]
            for y in range(numberOf_PSU_Tickets):                                           
                ticketImagePath.append(makeTheTicket('PSU'))                         # Make a PSU Student ticket and add it to ticketImagePath list

        if(spreadSheet['# of Non-PSU Tickets'][x] > 0): 
            numberOf_NonPSU_Tickets = spreadSheet['# of Non-PSU Tickets'][x]                                           
            for y in range(numberOf_NonPSU_Tickets):
                ticketImagePath.append(makeTheTicket('Non_PSU'))                     # Make a Non-PSU Student ticket and add it to ticketImagePath list
        
        em.Email.SendAnEmail(spreadSheet['PSU Email'][x], ticketImagePath)           # Call to method in Email Members Class called Send Email. Takes 2 properties (A email that is found in the PSU Email cell and the list that stores all the paths to the images of the tickets)
        x+=1



def makeTheTicket(kindOfTicket):                                                     # Method to make ticket based of excel info
                                                  
    f = open('NumberOf_TicketsSolds.txt','r')                                        # Opens text file that is keeping track of number of tickets sold in read only mode
    numberFromFile = f.read()                                                    
    number = int(numberFromFile)                                                 
    number+=1                                                                        # Since file starts from 0 tickets sold in order to get proper number on ticket need to +1 to the value from the text file
    ticketNumber = str(number)
    f.close()                                                                        # Closing file

    digits = 0

    while number != 0:                                                               # Determines the amount of digits in the ticket number 
        number //= 10
        digits += 1

    ticket = tm.TicketMaker.MakeTicket(ticketNumber,digits,kindOfTicket)             # Calling on method from TicketMakerClass to make the ticket image and returns the image

    f = open('NumberOf_TicketsSolds.txt','w')                                        # Opens text file that is keeping track of number of tickets sold and clears the document so new value can be now written
    fNumber = int(numberFromFile, base=0)                                        
    fNumber+=1
    f.write(str(fNumber))                                                            # Adds to number of tickets sold document
    f.close()

    return ticket                                                                    # Returns image path of the ticket image
    


ReadExcelAndMakeEmail()