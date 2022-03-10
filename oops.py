class Car:
    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year
    def printdata(self):
        print(self.model)
        print(self.color)
        print(self.year)

bmw = Car("3series","red","2020")
benz = Car("c class","white","2021")

bmw.printdata()
