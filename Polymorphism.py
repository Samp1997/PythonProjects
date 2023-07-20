#parent class
class User:
    name = "Sam"
    email = "sam@gamail.com"
    password = "4321abcd"

    def getLoginInfo(self):
        entry_name = input("Enter name: ")
        entry_email = input("Enter email: ")
        entry_password = input("Enter password: ")
        if (entry_email == self.email and entry_password == self.password):
             print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#Child Class
class Employee(User):
    base_pay = 11.00
    department = "Geneal"
    pin_number = "6824"


    def getLoginInfo(self):
        entry_name = input("Enter name: ")
        entry_email = input("Enter email: ")
        entry_pin = input("Enter pin: ")
        if (entry_email == self.email and entry_password == self.password):
             print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")


customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
