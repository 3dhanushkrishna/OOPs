class Person(object):
    def __init__(self,name,aadhar,phone):
        self.name = name
        self.aadhar = aadhar
        self.phone = phone
    def displaydetails(self):
        print(self.name+"\n"+self.aadhar+"\n"+self.phone)
class Employee(Person):
    def __init__(self,name,aadhar,phone,salary,designation):
        self.salary = salary
        self.designation = designation

        Person.__init__(self,name,aadhar,phone)
    def printdetails(self):
        print("name: ",self.name)
        print("aadhar: ",self.aadhar)
        print("phone: ",self.phone)
        print("salary: ",self.salary)
        print("designation: ",self.designation)
x = Employee("DHANUSH","434664","9843492484","45000","SOFTWARE")
x.printdetails()
y=Person("sameer","43454","3948547")
y.displaydetails()