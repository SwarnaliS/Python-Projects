
from abc import ABC, abstractmethod


#creating class
class Customer(ABC):
    def totalPurchase(self, amount): #defining method of Customer class.
        print ('Your total cost is:',amount)
    @abstractmethod
    def cardPayment(self, amount): # Defining abstract method. this will as for an argument but won't tell what kind of data it is.
        pass

class Person(Customer): # creating Child class.
    def cardPayment(self, amount):
        print ('Total cost of ${} exceeed the pre-set value of $100.00'.format(amount))



obj = Person()
obj.totalPurchase (400)
obj.cardPayment (400)

    
    
    
