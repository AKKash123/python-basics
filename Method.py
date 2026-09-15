class Student:  #parent class
    #init method intialised the instance of the class
    def __init__(self, name,marks):
        self.name = name    #declaration and assigining the value
        self.marks = marks

    def Show_Details(self):
        print("This is a student details:\n")
        print(f"Name: {self.name} Marks Obtain:{self.marks}")
#object creation and initialisation
s1 = Student("Rajib",86)  #constructor a method name is similar to the classname
s1.Show_Details()   #object call its class member
