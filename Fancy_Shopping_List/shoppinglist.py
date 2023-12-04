class ShoppingList():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.__PriceList()

    def __PriceList(self):
        if self.name == "Dry Cured Iberian Ham":
            self.standard_price = 177.8
        elif self.name == "Wagyu Steaks":
            self.standard_price = 450.0
        elif self.name == "Matsutake Mushrooms":
            self.standard_price = 272.0
        elif self.name == "Kopi Luwak Coffee":
            self.standard_price = 306.5
        elif self.name == "Moose Cheese":
            self.standard_price = 487.2
        elif self.name == "White Truffles":
            self.standard_price = 3600.0
        elif self.name == "Blue Fin Tuna":
            self.standard_price = 3603.0
        else:
            self.standard_price = 270.81

    def calculate(self):
        return self.standard_price * self.amount

    def getName(self):
        return self.name

    def getAmount(self):
        return self.amount

    def getPrice(self):
        return self.standard_price