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

#Child class
class Hours(User):
    Weekdays = "8 Am - 4 PM"
    Weekends = "Not Scheduled Weekends"

    def Workinghours(self):
        Weekdays = input ("What day/Schedule do you have:")
        if (Weekdays == self.Weekdays and Weekends == self.Weekends):
            print("Welcome back have a nice day!")
        else:
            print("You dont work today!")


    def getLoginInfo(self):
        entry_name = input("Enter name: ")
        entry_email = input("Enter email: ")
        entry_pin = input("Enter pin: ")
        Weekdays = input ("What day/Schedule do you have:")
        
        if (entry_email == self.email and entry_pin == self.pin_number):
             print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")


customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

person = Hours()
person.Workinghours()
