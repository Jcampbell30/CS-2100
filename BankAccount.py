class BankAccount:
    #magic method /called automatically
    def __init__(self,balance):
        self._balance = balance
    def deposit(self, amount):
        self._balance += amount
    def withdrawal(self, amount):
        self._balance -=amount
    def getBalance(self):
        return self._balance
    def __str__(self):
        return ("$" + "{0:,.2f}".format(self.getBalance()))
        


