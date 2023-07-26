#setting the class
class Protected:
    def __init__(self):
        self.__privateVar = 50
# child class
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
# the private variable that is set to be retreved from the classes above
obj = Protected()
obj.getPrivate()
obj.setPrivate(25)
obj.getPrivate()
