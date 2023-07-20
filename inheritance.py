#name of the parent class
class man:
    name = 'sam'
    Age = 26
    height = '6ft 5in'

    def information(self):
        msg = "Name: {}\n Age: {} \nHeight: 6ft 6in"
        return msg

#child class
class info(man):
    #Attributes
    hometown = 'Las Vegas'
    highschool = 'Green Valley high school'

    def information(self):
        msg = "\nI grew up in Las Vegas, and went to Greenvalley high school"
        return msg

    

# child class 
class People(info):
    M = 'Man'
    W = 'Women'

    def human(self):
            msg = "I am a man and not a women"
            return msg
    

if __name__ == "__main__":
    man = man()
    print(man.information())
    print(info.information())
