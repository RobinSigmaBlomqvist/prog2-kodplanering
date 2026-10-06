import random

class Product:
    def __init__(self, namn, price):
        self.namn = namn
        self.price = price

    def __str__(self):
        return self.namn

class Coffee(Product):
    def __init__(self):
        super().__init__("kaffe", 20)

class Cookie(Product):
    def __init__(self):
        super().__init__("kaka", 50)

class Cake(Product):
    def __init__(self):
        super().__init__("tårta", 100)

koffe = Coffee
cooki = Cookie
cake = Cake

class Player:
    def __init__(self, namn, pengar=200):
        self.namn = namn
        self.pengar = pengar

class Costumer:
    def __init__(self, want=None):
        self.want = None
        if want is not None:
            self.want = want
        else:
            self.set_want()

    def set_want(self, want=None):
        if want is not None:
            self.want = want
            return self.want

        produkter = [Coffee(), Cookie(), Cake()]
        self.want = random.choice(produkter)
        return self.want


player = Player("Klas")
dude = Costumer()
kokphase = False
buyphase = True


print(f"{player.namn} har {player.pengar} kronor.")

takunder = str(input("Vill du börja ta emot kunder?"))
if takunder == "ja":
    kokphase = True
    buyphase = False

while kokphase==True:
    print(f"Kunden vill ha: {dude.want}")
    kokphase=False