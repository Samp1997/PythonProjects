#name of the class
class People:
    name = 'sam'
    Age = 26
    height = '6ft 5in'
#The info class inherits from the People class
class info(People):
    #Attributes
    hometown = 'Las Vegas'
    highschool = 'Green Valley high school'

# child class that inherits the parent class
class Man(People):
    name = 'sam'
    Age = 26
    height = '6ft 5in'

print(Man)
