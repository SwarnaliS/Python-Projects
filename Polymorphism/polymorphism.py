#Creating parent class
class user:
    name = ''
    email = ''
    password = ''
    #Defininf method
    def login_info(self):
        Name = input("Please enter your name")
        Email = input ("Please enter your email")
        Password = input ("Please enter your password")
        if (Password==self.password ):
            print('Welcome {}, to the system'.format(Name))
        else:
            print('Your password is incorrect')
#Creating a child class
class employee(user):
    base_pay= 15.00
    department = ''
    e_pin = ''
    #Defining method with polymorphism 
    def login_info(self):
        Name = input("Please enter your name")
        Email = input ("Please enter your email")
        Pin = input ("Please enter your pin to log in to the system")
        if (Pin==self.e_pin ):
            print('Welcome {}, to the system'.format(Name))
        else:
            print('Your pin is incorrect')

#Creating another child class
class customer(user):
    cust_id = ''
    cust_group = ''
    
    #Defining method with polymorphism 
    def login_info(self):
        Name = input("Please enter your name")
        Email = input ("Please enter your email")
        Customer_Id= input ("Please enter your customer Id to log in to the system")
        if (Cutomer_Id==self.cust_id ):
            print('Welcome {}, to the system'.format(Name))
        else:
            print('Your pin is incorrect')
    
    
