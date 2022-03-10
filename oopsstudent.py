class Student:
    def __init__(self,name,rollno,admno,college):
        self.name = name
        self.rollno = rollno
        self.admno = admno
        self.college = college
    def printdata(self):
        print(self.name)
        print(self.rollno)
        print(self.admno)
        print(self.college)

student1 = Student(input("enter the name: "),input("enter the rollno: "),input("enter the admno: "),input("enter the college:"))
student2 = Student(input("enter the name: "),input("enter the rollno: "),input("enter the admno: "),input("enter the college:"))

student1.printdata()
student2.printdata()