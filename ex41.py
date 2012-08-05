class CashRegister(object):
    """A CashRegister object can do everything a real cash register can"""
    def __init__(self):
        """Initialize variables, and maybe something else?"""
        self.total = 0      # Variable for running total
        self.items = {}     # Dict for building an inventory of the items and their costs 
        self.lastChargeAdded = 0    # Variable which contains the last amount added to the bill
        self.receiptItems = [] # List which will contain lists containing Item name and Quantity.

    def scanItem(self):
        scanItem = raw_input("What is the item?  >> ")
        if scanItem == "total":
            print "\n"
            return False
        else: 
            scanQuantity = float(raw_input("How many are being purchased?  >> "))
            cr.addItem(scanItem, scanQuantity)
            return True

    def addItem(self, item, quantity):
        """Add an item to the bill, and set the lastChargeAdded to that amount.  If the item being added is not in the items Dict, the cash register asks for the price and adds it."""
        if item not in self.items:
            self.items[item] = float(raw_input ("What is the price of 1 unit of %s?  >> " % item))
        self.total += self.items[item] * quantity
        self.lastChargeAdded = self.items[item] * quantity
        self.receiptItems += (item, quantity)

    def formatTotal(self):
        """Displays the total with a currency indicator."""
        currencySymbol = "$"
        return "The total is %s%.2f" % (currencySymbol,self.total)

    def printReceipt(self):
        """Prints a header; the items purchased, their quantity, and the total for each item; a subtotal, discounts, taxes, the total, the method of payment, payment details (incl. change if applicable), and finally a footer"""
        header = "Connor's Cash-Only Emporium"
        receipt = [header,self.receiptItems,self.formatTotal()]
        return receipt

############### END CashRegister OBJECT CLASS DEFINITION ################
    
cr = CashRegister()

keepScanning = True
while keepScanning:
    keepScanning = cr.scanItem()

for line in cr.printReceipt():
    print (line)
