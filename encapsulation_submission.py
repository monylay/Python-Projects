

#create a class
class BankAccount:

    def __init__(self, name, balance):

        #public attribute
        self.name = name

        #protected attribute, single underscore means protected
        self._balance = balance

        #private attribute, two underscore means harder access
        self.__pin = 5678

    #method to display protected balance
    def getBalance(self):
        print("Balance: ", self._balance)

    #method to display private PIN
    def getPin(self):
        print("PIN: ", self.__pin)

#create an object from bankaccount class
account = BankAccount("Pomi", 1500)

#object's public attribute
print(account.name)

#method that access the protected attribute
account.getBalance()

#method that access the private attribute
account.getPin()
