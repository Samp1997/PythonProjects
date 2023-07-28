from abc import ABC, abstractmethod
class budget(ABC):
    def Total(self, amount):
        print("Your Total is: ",amount)
    #function that passes an argument
    @abstractmethod
    def payment(self, amount):
        pass



class PaymentAmount(budget):
    #The defined amount to implement for the budget function from the budget class
    def payment(self, amount):
        print('Your Total amount of {} exceedes your budget of $100 limit '.format(amount))

obj = PaymentAmount()
obj.Total("$300")
obj.payment("$300")
