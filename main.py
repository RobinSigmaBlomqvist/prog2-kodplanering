import random


class Product:
    def __init__(self, namn, byprice, sellprice):
        self.namn = namn
        self.byprice = byprice
        self.sellprice = sellprice

    def __str__(self):
        return self.namn


class Coffee(Product):
    def __init__(self):
        super().__init__("kaffe", 5, 10)


class Cookie(Product):
    def __init__(self):
        super().__init__("kaka", 10, 20)


class Cake(Product):
    def __init__(self):
        super().__init__("tårta", 20, 40)


class Player:
    def __init__(self, namn, pengar, harkaffe, hartårta, harkaka):
        self.namn = namn
        self.pengar = pengar
        self.harkaffe = harkaffe
        self.hartårta = hartårta
        self.harkaka = harkaka


class Customer:
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


player = Player("Klas", 200, 0, 0, 0)
kokphase = False
buyphase = True
life = True

kaffe = Coffee()
kaka = Cookie()
tårta = Cake()

print(f"{player.namn} har {player.pengar} kronor.")

while life:
    while buyphase:
        print("[Kaffe 5kr] [Kaka 10kr] [Tårta 20kr]")
        köper = input("Vad vill du köpa? ").strip().lower()

        if köper == "kaffe":
            if player.pengar >= kaffe.byprice:
                player.harkaffe += 1
                player.pengar -= kaffe.byprice
            else:
                print("Du är för fattig")

        elif köper == "kaka":
            if player.pengar >= kaka.byprice:
                player.harkaka += 1
                player.pengar -= kaka.byprice
            else:
                print("Du är för fattig")

        elif köper == "tårta":
            if player.pengar >= tårta.byprice:
                player.hartårta += 1
                player.pengar -= tårta.byprice
            else:
                print("Du är för fattig")

        else:
            print("Finns inte")

        print(
            f"Du har [{player.harkaffe}] Kaffe, "
            f"Du har [{player.harkaka}] Kaka, "
            f"Du har [{player.hartårta}] Tårta, "
            f"Du har [{player.pengar}] pengar"
        )

        takunder = input("Vill du börja ta emot kunder? ").strip().lower()
        if takunder == "ja":
            kokphase = True
            buyphase = False

    happykund = 0
    sadkund = 0

    while kokphase:
        dude = Customer()
        print("")
        print(
            f"Du har [{player.harkaffe}] Kaffe, "
            f"Du har [{player.harkaka}] Kaka, "
            f"Du har [{player.hartårta}] Tårta, "
            f"Du har [{player.pengar}] pengar"
        )
        print(f"Kund: Hej, jag vill ha {dude.want.namn}")

        ge = input(f"Vill du ge kunden {dude.want.namn}? ").strip().lower()
        if ge == "ja":
            if isinstance(dude.want, Coffee):
                if player.harkaffe > 0:
                    player.harkaffe -= 1
                    player.pengar += dude.want.sellprice
                    happykund += 1
                    print("Yumyum")
                else:
                    print("Tyvärr har vi ingen mer kaffe")
                    sadkund += 1
            elif isinstance(dude.want, Cookie):
                if player.harkaka > 0:
                    player.harkaka -= 1
                    player.pengar += dude.want.sellprice
                    happykund += 1
                    print("Yumyum")
                else:
                    print("Tyvärr har vi ingen mer kaka")
                    sadkund += 1
            elif isinstance(dude.want, Cake):
                if player.hartårta > 0:
                    player.hartårta -= 1
                    player.pengar += dude.want.sellprice
                    happykund += 1
                    print("Yumyum")
                else:
                    print("Tyvärr har vi ingen mer tårta")
                    sadkund += 1
        else:
            sadkund += 1

        stänga = input("Klar för dagen? ").strip().lower()
        if stänga == "ja":
            kokphase = False
            bonus = happykund ** 2 - sadkund * 3
            player.pengar += bonus
            print(f"Du hade {happykund} nöjda kunder idag och {sadkund} missnöjda kunder")
            print(f"Din bonus blir då [{bonus}]")
            print(f"Du har nu {player.pengar} kronor.")
            buyphase = True
            break

        if not kokphase:
            break
