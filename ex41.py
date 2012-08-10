#! /usr/bin/env python

"""ex41 is supposed to be a game, and it is a game of sorts, but I guess I just wanted to play with objects in python some more, so I made this.
This file implements a CashRegister object, and when run boots a Cash Register object.  Further instructions are in the program when it's run."""


# Import statements
import csv, datetime

date = datetime.datetime.now()


class CashRegister(object):
    """A CashRegister object tha can do everything a real cash register can"""


    def __init__(self):
        """Initialize variables, and printing the welcome message"""
        # Declaring variables that are empty or 0 to begin with
        self.total              =   0           # Variable for running total
        self.currentInventory   =   []          # Total inventory of goods
        self.lastChargeAdded    =   0           # Variable which contains the last amount added to the bill
        self.receiptItems       =   []          # List which will contain lists containing Item name and Quantity.
        self.invTitlesCSV       =   ""          # Titles for the Inventory CSV file

        # Declaring variables that will affect display
        self.currencySymbol =   "$"           # Localization
        self.nameWidth      =   24            # Sets the length of the item name used on the receipt
        self.storeName      =   "Connor's Cash-Only Emporium"       # Sets the store name in the receipt

        # Declaring variables that are created from functions
        
        # Dict for building an inventory of the items and their costs from the filename passed here
        self.fileName   =   "ex41inventory.csv"
        self.items      =   self.getInventory(self.fileName)

        # Print the introductory text
        print """
        Welcome to the Cash Register!

The system will automatically boot into scan mode, [currently that's the ONLY mode]
From there, you can enter items and quantities as prompted.

If no price exists in the system for the item you have entered, you will be asked to add one.
Once a price is added it will exist in the system for that item until the cash register is restarted.

To delete the last item added, you can use the command "void" at the "Which item?" prompt.
To complete the transaction and print the receipt, you can use the command "total" at the "Which item?" prompt.
"""
    


    def getInventory(self, fileName):
        """Retreives the stored inventory data from the inventory datafile, """
        with open(fileName, 'rb') as invData:
            inventoryData = csv.reader(invData, delimiter=',')
            itemLookup = {}

            for row in inventoryData:
                if row[0] == 'name':
                    print "Initializing inventory data..."
                    pass                                    # skip the first row
                else:
                    self.currentInventory.append(row)       # add all the other rows to the current inventory
        
            for item in self.currentInventory:              # for every item, generate a price dict lookup
                if item[3] == "FALSE":                      # If Item isn't on sale
                    itemLookup[item[0]] = float(item[1])    # get the regular price
                else:                                       # otherwise, get the sale price
                    itemLookup[item[0]] = float(item[2])

        return itemLookup                                   # return the dict for looking up prices



    def scanMode(self):
        """Asks for input and directs the register how to deal with it."""
       
        scanItem = raw_input("What is the item?  >> ")
               
        if "total" in scanItem:         # break the loop and complete the transaction
            print "\n"
            return False            # returning False breaks the loop
            
        elif "void" in scanItem:                # undo the last transaction processed
            self.voidItem()
            return True             # returning True continues the loop
            
        elif "createItem" in scanItem:          # add an intem to the inventory list
            self.createItem()
            return True             # returning True continues the loop
            
        else:                    # Otherwise, assume the input is an item name
            if scanItem not in self.items:      # checks if the item already has a price
                print "That item does not appear to be in the item database.  If you wish to add it, please enter createItem at the scanning prompt."
                return True
            else:
                try:
                    scanQuantity = float(raw_input("How many are being purchased?  >> "))
                except ValueError:
                    print "That is not a valid number, the quantity has defaulted to 1"
                    scanQuantity = 1

                self.addItem(scanItem, scanQuantity)    # add the item to the purchase
                return True                             # returning True continues the loop

                


    def addItem(self, item, quantity):
        """Add an item to the bill, and set the lastChargeAdded to that amount.  If the item being added is not in the items Dict, the cash register asks for the price and adds it."""
        if item in self.items:
            self.total += self.items[item] * quantity           # increase the total sales price
            self.lastChargeAdded = self.items[item] * quantity  # set the lastChargeAdded to this transaction
            self.receiptItems.append((item, quantity))          # add this transaction to the receipt
        else:
            print "That item does not appear to be in the item database.  If you wish to add it, please enter createItem at the scanning prompt."
    


    def createItem(self):
        """Adds a new item to the list of available items"""
        item = (raw_input("What item would you like to add?  >> "))
        newItem = [item,0,0,"FALSE",0,int(self.currentInventory[-1][5])+1]

        for x in range(1,2+1):      # Range is non-inclusive
            try:                    # it asks for a price, 
                print "What is the",
                if x == 1:
                    print "regular",
                else:
                    print "sale",
                newItem[x] = float(raw_input ("price of 1 unit of %s?  >> " % (item)))
            except ValueError:      # and will continue to ask until you give it one
                print "Sorry, that's not a proper price.  The format should be like 4.69 "


        onSale = raw_input("Is %s currently on sale?  ( y / n )  >> " % item)[:1]
        if (onSale == "y") or (onSale == "Y"):  # Find out if the product is on sale
            newItem[3] = "TRUE"
        else:                                   # record the answer
            newItem[3] = "FALSE"

        while True:
            try:                    # Asks for the inventory quantity
                newItem[4] = float(raw_input("How many %s are in stock?  >> " % item))
                break
            except ValueError:      # until it works
                print "That is not a valid quantity.  Pretty much any number will do"
        
        if newItem[3] == "FALSE":               # If the new item is not on sale
             self.items[item] = newItem[1]      # Add the regular price to the inventory Dict
        else:
             self.items[item] = newItem[2]      # otherwise add the regular price to the inventory Dict

        self.currentInventory.append(newItem)   # Add new item to current Inventory
        self.addItemToInventory(newItem)        # Write new item to inventory file
        print "\n%.3f units of %s have been added to the inventory with a regular price of %s, a sale price of %s, and a sku of %d.  The item is currently %son sale.\n" % (newItem[4], newItem[0], self.currency(newItem[1]), self.currency(newItem[2]),newItem[5], self.onSale(newItem[3]))



    def onSale(self, onSale):
        """ Returns text value for item creation confirmation string. """
        if onSale == "FALSE":
            return "not "
        else:
            return ""



    
    def addItemToInventory(self, newItem):
        """Adds a new item to the inventory data file"""
        with open(self.fileName, 'ab') as invFile:
            invFileWrite = csv.writer(invFile)
            invFileWrite.writerow(newItem)



    def voidItem(self):
        """Voids the most recent transaction"""
        try:                                                                    # unless there is nothing in the list of items to be included on the receipt
            void = self.receiptItems.pop()                                      # remove the last item on the list
            self.total -= self.items[void[0]] * void[1]                         # reduce the total by the appropriate amount
            print "%.3f of item: %s have been removed." % (void[1],void[0])     # print confirmation of the void
        except IndexError:  
            print "There is nothing to void, the list of items scanned is empty."



    def currency(self,amount):
        """takes a single number as an argument, returns a string of that number formatted as currency"""
        return "%s%.2f" % (self.currencySymbol,float(amount))



    def formatTotal(self):
        """Displays the total with a currency indicator."""
        return "The subtotal is %s" % (self.currency(self.total))



    def printReceipt(self):
        """Prints a header; the items purchased, their quantity, and the total for each item; a subtotal, discounts, taxes, the total, the method of payment, payment details (incl. change if applicable), and finally a footer"""
        receipt = []
        for line in self.printHeader():         # Go look at the printHeader method.  This prints each line of that.
            receipt.append(line)

        for item in self.receiptItems:                              # for each item scanned
            formattedItem = "%10s  of  %s at %12s  is  %12s" % ("%.3f" % (item[1]),item[0].ljust(self.nameWidth)[:self.nameWidth], self.currency(self.items[item[0]]), self.currency(float(item[1])*self.items[item[0]])) 
            # create a string that contains -                   # the quantity      # The item name, to set width                   # The per-unit cost, and            # The total cost (per-unit cost * # of units)
            receipt.append(formattedItem)                           # add the formattedItem string to the receipt

        receipt.append(self.formatTotal().rjust(50 + self.nameWidth) + "\n")    # Display Subtotal
        receipt.append("Thank you for shopping at:\t%s\n" % (self.storeName))   # This is a simple footer
        return receipt


    def printHeader(self):
        """Assembles and returns a list of strings that make up the receipt header."""
        header = []
        header.append("\t\t%s" % (self.storeName))          # Indent and display the store name
        header.append(date.strftime("%H:%M:%S %d-%b/%y"))   # Display a formated date/time string ( 23:59:59 31-Dec/99 )

        header.append("\n")                                 # Insert a blank line
        return header




############### END CashRegister OBJECT CLASS DEFINITION ################


    
cr = CashRegister()

keepScanning = True
while keepScanning:
    keepScanning = cr.scanMode()  # load the CashRegister into scanMode

for line in cr.printReceipt():      # ask the CashRegister to end the transaction and print a receipt
    print("\t"),
    print (line)

# ADMIN MODE COMMAND 
