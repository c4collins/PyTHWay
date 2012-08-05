class CashRegister(object):
    """A CashRegister object can do everything a real cash register can"""
    def __init__(self):
        """Initialize variables, and maybe something else?"""
        self.total = 0      # Variable for running total
        self.items = {}     # Dict for building an inventory of the items and their costs 
        self.lastChargeAdded = 0    # Variable which contains the last amount added to the bill
        self.receiptItems = [] # List which will contain lists containing Item name and Quantity.
        self.currencySymbol = "$"   # Localization

    def scanItem(self):
        scanItem = raw_input("What is the item?  >> ")[:30]
        if scanItem == "total":
            print "\n"
            return False
        else if scanItem == "void":
            self.voidItem()
            return True
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
        self.receiptItems.append((item, quantity))

    def voidItem(self):
        """Voids the most recent transaction"""
        print receiptItems[len(receiptItems)]







    def currency(self,amount):
        return "%s%.2f" % (self.currencySymbol,amount)

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
            item[0]+" "*(30-len(item[0])), \
            self.currency(self.items[item[0]]),\
            self.currency(float(item[1])*self.items[item[0]])\
            )

            receipt.append(formattedItem)

        receipt.append(self.formatTotal().rjust(80))
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
