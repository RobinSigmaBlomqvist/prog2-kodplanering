class Player:
    def __init__(self, namn):
        self.namn = namn

player = Player("Clas")

class Product:
    def __init__(self, namn, price):
        self.namn = namn
        self.price = price

class Koffe(Product):
    def __init__(self):
        super().__init__("kaffe", 20)

class cooki(Product):
    def __init__(self):
        super().__init__("kaka", 50)

class cake(Product):
    def __init__(self):
        super().__init__("tårta", 100)

kaka = cooki()
tårta = cake()

print(kaka.namn, tårta.price)