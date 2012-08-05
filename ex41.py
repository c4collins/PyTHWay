class CashRegister(object):

    def __init__(self):
        self.total = 0
        self.inventory = {}
        self.lastChargeAdded = 0

    def addItem(self, item, quantity):
        if item not in self.inventory:
            self.inventory[item] = float(raw_input ("What is the price of 1 unit of %s?  >" % item))
        self.total += self.inventory[item] * quantity
        self.lastChargeAdded = self.inventory[item] * quantity

    def formatTotal(self):
        return "The total is $%g" % self.total
        
cr = CashRegister()

print cr.total
cr.addItem("Banana", 4)
print cr.total
print cr.formatTotal()
