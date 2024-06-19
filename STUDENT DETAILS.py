class Student:
    def _init_(self):
        self.Name=None
        self.usn=None
        self.total=None
        self.percentage=None
        self.grade=None
    def inputs(self):
        self.name=input("Enter the name")
        self.usn=input("Enter the usn")
        self.marks=[]
        for i in range(5):
            ele=int(input(f"Enter the marks for subject{i+1}"))
            self.marks.append(ele)
    def percent(self):
        self.percentage=(sum(self.marks) /500)*100
        
    def grades(self):
        if(self.percentage>90):
            self.grade='A'
        elif(90>self.percentage and self.percentage>60):
            self.grade='B'
        elif(30>self.percentage and self.percentage>20):
            self.grade='C'
        else:
            self.grade='F'
    def display(self):
        print(f"Name:{self.name}\tUSN:{self.usn}\tPercentage:{self.percentage}\tGrade:{self.grade}")
        
     

obj=Student()
obj.inputs()
obj.percent()
obj.grades()
obj.display()
