
#Parent class User
class User:
    name = "Pomi"
    email = "Pomi@gmail.com"
    password = "Pomi12345"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

#This is the same method in the parent class "User"
#the difference is that, instead of using entry_password, we're using entry_pin


    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")

#Child class Admin
class Admin(User):
    admin_code = "ADMIN456"

    #override getLoginInfo method
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_code = input("Enter your admin code: ")

        if (entry_email == self.email and entrry_code == self.admin_code):
            print("Welcome back, Admin {}!".format(entry_name))
        else:
            print("The admin code or email is incorrect.")

#The following code invokes the methods inside each class for User and Employee

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

administrator = Admin()
administrator.getLoginInfo()
