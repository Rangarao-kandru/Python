######### Gender #########

"""2.Define a class Person and its two child classes: Male and Female.
 All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
"""

class Person:
    def getGender(self):
        print('unknown')

class Male(Person):

    def getGender(self):
        print('Male')

class Female(Person):
    def getGender(self):
        print('Female')

m = Male()
m.getGender()
f = Female()
f.getGender()
© 2020 GitHub, Inc.

    def __repr__(self):
        return "'self.getX()== self.getY() '"


a = int(input("enter x coordinate:"))
b = int(input("enter y coordinate:"))
obj = Coordinate(a, b)
print(obj.__str__())
print(a == b)
print(eval(repr(obj)))

