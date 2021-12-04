#Creating Student class
class student:
    # Initialising an object
    def __init__(self,name,grade,school,email):
        self.name = name
        self.grade = grade
        self.school = school
        self.email = email
   
#Defining a method
    def information(self):
        info = self.name,self.grade,self.school,self.email
        return info

    
#Creating an object
new_student = student('Henry Thomas','2nd','Vista Elementary','parent.Thomas@hotmail.com')

if __name__ == '__main__':
   print(f'{new_student.name} is attending {new_student.school}')
