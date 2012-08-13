#! /usr/bin/env python

"""ex41 is supposed to be a game, and it is a game of sorts, but I guess I just wanted to play with objects in python some more, so I made this.
This file implements a CashRegister object, and when run boots a Cash Register object.  Further instructions are in the program when it's run."""


# Import statements
import csv, datetime

# Global variables
date = datetime.date.today()

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
        self.taxName        =   "HST/GST"     # Localization
        self.taxRate        =   0.13        # Localization
        self.nameWidth      =   24            # Sets the length of the item name used on the receipt
        self.storeName      =   "Connor's Cash-Only Emporium"       # Sets the store name in the receipt
        self.storeAddress   =   ["123 Fake St.","Waterloo, ON", "N2V 2L4 Canada"]

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

To delete the last item added, you can use the command "void" at the "Which item?" prompt.  You can also specify voiding an item earlier than the last item by entering how far back the transaction is.  The second last item would be 2, the third last would be 3, etc.  You can also start from the beginning of the list, but with negative numbers: 0 is the first item scanned, -1 is the second item scanned, etc.

To complete the transaction and print the receipt, you can use the command "total" at the "Which item?" prompt.
"""
    


    def getInventory(self, fileName):
        """Retrieves the stored inventory data from the inventory datafile, """
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
        scanItem = raw_input("What is the item?  >> ").strip()
        if scanItem == "total":     # If the command 'total' is given, break the loop and complete the transaction
            print "\n"
            return False            # returning False breaks the loop
        elif scanItem == "void":    # If the command 'void' is given, undo the last transaction processed
            self.voidItem()
            return True             # returning True continues the loop
        elif "void" in scanItem:
            trash, num = scanItem.split(" ")
            self.voidItem(-int(num))
            return True 
        elif scanItem == "createItem":
            cr.createItem(raw_input("What item would you like to add?  >> "))
            return True
        else:                       # Otherwise, assume the input is an item name
            if scanItem in self.items:
                try:
                    scanQuantity = float(raw_input("How many are being purchased?  >> "))
                except ValueError:
                    print "That is not a valid number, the quantity has defaulted to 1"
                    scanQuantity = 1
    
                self.addItem(scanItem, scanQuantity)    # add the item to the purchase
                return True                             # returning True continues the loop
            else:
                print "Sorry, that item is not currently in stock, or is not part of the inventory.  Please try again."
                return True            


    def addItem(self, item, quantity):
        """Add an item to the bill, and set the lastChargeAdded to that amount."""
        self.total += self.items[item] * quantity           # increase the total sales price
        self.lastChargeAdded = self.items[item] * quantity  # set the lastChargeAdded to this transaction
        self.receiptItems.append((item, quantity))          # add this transaction to the receipt



    def createItem(self, item):
        """Adds a new item to the list of available items"""
        newItem = [item,0,0,"FALSE",0,int(self.currentInventory[-1][5])+1]
        while True:
            try:                    # it asks for a price, 
                newItem[1] = float(raw_input ("What is the regular price of 1 unit of %s?  >> " % item))
                break
            except ValueError:      # and will continue to ask until you give it one
                print "Sorry, that's not a proper price.  The format should be like 4.69 "

        while True:
            try:                    # It asks for a sale price
                newItem[2] = float(raw_input ("What is the sale price of 1 unit of %s?  >> " % item))
                break
            except ValueError:      # And does not accept no for an answer
                print "Sorry, that's not a proper price.  The format should be like 4.69 "
        
        onSale = raw_input("Is %s currently on sale?  ( y / n )  >> " % item)[:1]
        if (onSale == "y") or (onSale == "Y"): # Asks what the sale "boolean" value should be set to
            newItem[3] = "TRUE"
        else:
            newItem[3] = "FALSE"

        while True:
            try:                    # Asks for the stock quantity of the item being added
                newItem[4] = float(raw_input("How many %s are in stock?  >> " % item))
                break
            except ValueError:      # Patiently waits until an appropriate answer is given.
                print "That is not a valid quantity.  Pretty much any number will do"
        
        if newItem[3] == "FALSE":       # If the item is not on sale
             self.items[item] = newItem[1]      # load the regular price into the price check list
        else:
             self.items[item] = newItem[2]      # Otherwise, load the sale price

        self.currentInventory.append(newItem)   # Adds the new item to the inventory-in-memory
        self.addItemToInventory(newItem)        # Adds the new item to the inventory date file
        print newItem


    
    def addItemToInventory(self, newItem):
        """Adds a new item to the inventory data file"""
        with open(self.fileName, 'ab') as invFile:
            invFileWrite = csv.writer(invFile)
            invFileWrite.writerow(newItem)



    def voidItem(self, index = -1):
        """Voids the most recent transaction"""
        try:                                                                    # unless there is nothing in the list of items to be included on the receipt
            void = self.receiptItems.pop(index)                                      # remove the last item on the list
            self.total -= self.items[void[0]] * void[1]                         # reduce the total by the appropriate amount
            print "%.3f of item: %s have been removed." % (void[1],void[0])     # print confirmation of the void
        except IndexError:  
            print "There is nothing in the list at that postion."
            try:
                print "The most recent item in the list is: %s" % self.items[-1][0]
            except IndexError:
                print "There are no items currently accumulated on this register."



    def currency(self,amount,precise=False):
        """takes a single number as an argument, returns a string of that number formatted as currency"""
        if ("%.2f" % float(amount) == "0.00") and (precise==True):
            return "%s%.3f" % (self.currencySymbol,float(amount))
        else:
            return "%s%.2f" % (self.currencySymbol,float(amount))
           



    def printReceipt(self):
        """Prints a header; the items purchased, their quantity, and the total for each item; a subtotal, discounts, taxes, the total, the method of payment, payment details (incl. change if applicable), and finally a footer"""
        receipt = []

        for line in self.printReceiptHeader():
            receipt.append(line.center(55 + self.nameWidth))
        for line in self.printReceiptItems():
            receipt.append(line)
        for line in self.printReceiptTotal():
            receipt.append(line)


#        receipt.append(self.formatTotal().rjust(50 + self.nameWidth) + "\n")    # Display Subtotal
        receipt.append("Thank you for shopping at:\t%s\n" % (self.storeName))   # This is a simple footer
#        print self.receiptHeader()
        return receipt

    

    def printReceiptHeader(self):
        """Returns the receipt header text as a list of strings"""
        header = []

        header.append("Thank you for shopping at:")
        header.append("")
        header.append("%s" % self.storeName.upper())
        header.append("")

        for item in self.storeAddress:
            header.append("%s" % item)

        header.append("")
        header.append(date.strftime("%d-%h/%Y"))
        header.append("")

        return header



    def printReceiptItems(self):
        """Returns each item in the receiptItems list as a formatted string for the receipt"""
        items = []

        items.append("="*(55 +self.nameWidth))
        items.append("%10s      %s%18s%12s" % ("Quantity","Item".ljust(self.nameWidth),"Per Unit","Price"))  #  Header Row
        items.append("="*(55 +self.nameWidth))

        for item in self.receiptItems:                              # for each item scanned
            formattedItem = "%10s  of  %s at %12s  is  %12s" % ("%.3f" % (item[1]),item[0].ljust(self.nameWidth)[:self.nameWidth], self.currency(self.items[item[0]],True), self.currency(float(item[1])*self.items[item[0]]))       # Create a string with the following information:
            # the quantity
            # The item name, to set width
            # The per-unit cost, and
            # The total cost (quantity * per-unit cost)
            
            items.append(formattedItem)                     # Add it to the list
       
        items.append("="*(55 +self.nameWidth))
        items.append("")
        
        if len(self.receiptItems) == 0:
            items[1] = "No items have been scanned".center(55+self.nameWidth)
            del items[2]
            

        return items



    def printReceiptTotal(self):
        """Displays the total with a currency indicator."""
        totalLines = []
        
        totalLines.append("The subtotal is %s".rjust(self.nameWidth) % (self.currency(self.total)))
        totalLines.append("The freight cost is %s".rjust(self.nameWidth) % (self.currency(0)))
        totalLines.append("The taxes (%s) is %s".rjust(self.nameWidth) % (self.taxName,self.currency(self.total*self.taxRate)))
        totalLines.append("")
        totalLines.append("="*(55+self.nameWidth))
        totalLines.append("The total is %s".rjust(self.nameWidth) % (self.currency(self.total*(1+self.taxRate))))
        
        return totalLines



############### END CashRegister OBJECT CLASS DEFINITION ################


    
cr = CashRegister()

keepScanning = True
while keepScanning:
    keepScanning = cr.scanMode()  # load the CashRegister into scanMode

for line in cr.printReceipt():      # ask the CashRegister to end the transaction and print a receipt
    print("\t"),
    print (line)

# ADMIN MODE COMMAND 
