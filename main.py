class Soda:
    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            if isinstance(self.additive, str):
                print (f"Газировка и {self.additive}")
            else:
                print ("Добавка должна быть строкой")
        else:
            print ("Обычная газировка")
    def __call__(self):
        self.show_my_drink()

    def __str__(self):
        if self .additive:
            if isinstance(self.additive, str):
                return f"Газировка и {self.additive}"
            else:
                return "Некорректная добавка(должна быть строкой)"
        else:
            return "Обычная газировка"
    def __repr__(self):
        return f"Soda(additive = {repr(self.additive)})"

drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda()

print(str(drink1))
print(str(drink2))
print(str(drink3))

print(repr(drink1))
print(repr(drink2))
print(repr(drink3))