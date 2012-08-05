#! /usr/bin/env python

"""ex41 is supposed to be a game, and it is a game of sorts, but I guess I just wanted to play with objects in python some more, so I made this.
This file implements a CashRegister object, and when run boots a Cash Register object.  Further instructions are in the program wehn it's run."""

import csv


class CashRegister(object):
    """A CashRegister object tha can do everything a real cash register can"""


    def __init__(self):
        """Initialize variables, and printing the welcome message"""
        self.total = 0      # Variable for running total
        self.items = self.getInventory("ex41inventory")     # Dict for building an inventory of the items and their costs 
        self.lastChargeAdded = 0    # Variable which contains the last amount added to the bill
        self.receiptItems = [] # List which will contain lists containing Item name and Quantity.
        self.currencySymbol = "$"   # Localization
        self.nameWidth = 24     # Sets the length of the item name used on the receipt

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
        """Retreives the stored inventory data from the inventory datafile"""
        inventoryData = csv.reader(open(fileName+".csv", 'rb'), delimiter=',')
        for row in inventoryData:
            print ', '.join(row)
        return {}

    def scanItem(self):
        scanItem = raw_input("What is the item?  >> ")
        if scanItem == "total":
            print "\n"
            return False
        elif scanItem == "void":
            self.voidItem()
            return True
        else: 
            try:
                scanQuantity = float(raw_input("How many are being purchased?  >> "))
            except ValueError:
                print "That is not a valid number, the quantity has defaulted to 1"
                scanQuantity = 1
            cr.addItem(scanItem, scanQuantity)
            return True
                

    def addItem(self, item, quantity):
        """Add an item to the bill, and set the lastChargeAdded to that amount.  If the item being added is not in the items Dict, the cash register asks for the price and adds it."""
        if item not in self.items:
            while True:
                try:
                    self.items[item] = float(raw_input ("What is the price of 1 unit of %s?  >> " % item))
                    break
                except ValueError:
                    print "Sorry, that's not a proper decimal number.  The format should be like 4.69 "
        self.total += self.items[item] * quantity
        self.lastChargeAdded = self.items[item] * quantity
        self.receiptItems.append((item, quantity))

    def voidItem(self):
        """Voids the most recent transaction"""
        try:
            void = self.receiptItems.pop()
            self.total -= self.items[void[0]] * void[1]
            print "%.3f of item: %s have been removed." % (void[1],void[0])
        except IndexError:
            print "There is nothing to void, the list of items scanned is empty."

    def currency(self,amount):
        """takes a single number as an argument, returns a string of that number formatted as currency"""
        return "%s%.2f" % (self.currencySymbol,float(amount))

    def formatTotal(self):
        """Displays the total with a currency indicator."""
        return "The total is %s" % (self.currency(self.total))

    def printReceipt(self):
        """Prints a header; the items purchased, their quantity, and the total for each item; a subtotal, discounts, taxes, the total, the method of payment, payment details (incl. change if applicable), and finally a footer"""
        receipt = []
        receipt.append("\t\tConnor's Cash-Only Emporium")
        for item in self.receiptItems:
            formattedItem = "%10s  of  %s  @ %12s  is  %12s" % (\
            "%.3f" % (item[1]),\
            item[0].ljust(self.nameWidth)[:self.nameWidth], \
            self.currency(self.items[item[0]]),\
            self.currency(float(item[1])*self.items[item[0]])\
            )

            receipt.append(formattedItem)

        receipt.append(self.formatTotal().rjust(50 + self.nameWidth) + "\n")
        receipt.append("Thank you for shopping at:\tConnor's Cash-Only Emporium\n")
        return receipt

############### END CashRegister OBJECT CLASS DEFINITION ################
    
cr = CashRegister()

keepScanning = True
while keepScanning:
    keepScanning = cr.scanItem()

for line in cr.printReceipt():
    print("\t"),
    print (line)
