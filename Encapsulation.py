class Government:
    def __init__(self):
        self.__price = 100
    def ViewPetrolPrice(self):
        print(self.__price)
    def hikeprice(self,price):
        self.__price = price
CentralGovt=Government()
CentralGovt.ViewPetrolPrice()
CentralGovt.__price = 130
CentralGovt.ViewPetrolPrice()
CentralGovt.hikeprice(120)
CentralGovt.ViewPetrolPrice()

