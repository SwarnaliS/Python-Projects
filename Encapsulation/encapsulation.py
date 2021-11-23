
#creating the class
class Protected:
    def __init__(self):
        self._protectedVar=0 # using single underline to make a protected variable.
    

#Creating an object
obj = Protected()
obj._protectedVar=58
print(obj._protectedVar)


#Creating a class
class Private:
    def __init__(self):
        self.__privateVar=15 #Using double underlines to make a private variable.

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__private = private
        

obj = Private()
obj.getPrivate()#Calling the variable.
obj.setPrivate(48)#Setting a new value to the private variable
obj.getPrivate()#calling the new value
