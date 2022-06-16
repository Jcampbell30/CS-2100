#@Author: Jared Campbell
#Date: 06/15/22

class Currency:

    def __init__(self,currencyType,l_or_r,switched,amount):
        self._currencyType = currencyType
        self._l_or_r = l_or_r
        self._switched = switched
        self._amount = amount
   
    def __str__(self):
        if self._switched:
            if self._l_or_r:
                return "{0:s}{1:,.2f}".format(self._currencyType , self._amount)
            else:
                return "{0:,.2f}{1:s}".format(self._amount, self._currencyType)
        else:
            if self._l_or_r:
                valid = "{0:s}{1:,.2f}".format(self._currencyType,self._amount)
                valid = valid.replace(",", "temp")
                valid = valid.replace(".",",")
                valid = valid.replace("temp", ".")
                return valid
            else:
                valid = "{0:,.2f}{1:s}".format(self._amount, self._currencyType)
                valid = valid.replace(",", "temp")
                valid = valid.replace(".",",")
                valid = valid.replace("temp", ".")
                return valid