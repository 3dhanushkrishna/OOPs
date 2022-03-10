class Student(object):
    def __init__(self,name,rollno,admno,college):
        self.name = name
        self.rollno = rollno
        self.admno = admno
        self.college = college
    def getdetails(self):
        print("name: ",self.name+"\n"+"rollno: ",self.rollno+"\n"+"admno: ",self.admno+"\n"+"college: ",self.college)
class Exam(Student):
    def __init__(self,name,rollno,admno,college,examname,englishmark,mathsmark,physicsmark,chemistrymarks):
        self.examname = examname
        self.englishmark = englishmark
        self.mathsmark = mathsmark
        self.physicsmark = physicsmark
        self.chemistrymark = chemistrymarks
        Student.__init__(self,name,rollno,admno,college)
    def printdetails(self):
        print("name= ",self.name)
        print("rollno= ",self.rollno)
        print("admno= ",self.admno)
        print("college= ",self.college)
        print("examname= ",self.examname)
        print("englishmark= ",self.englishmark)
        print("mathsmark= ",self.mathsmark)
        print("physicsmark= ",self.physicsmark)
        print("chemistrymark= ",self.chemistrymark)

x=Exam("dhanush","2","23","ACE","MODEL","77","86","98","96")
y=Student("sameer","30","56","ACE")
x.printdetails()
y.getdetails()