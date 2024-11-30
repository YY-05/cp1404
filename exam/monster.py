TEETH = 16
COLOUR = "red"


class Monster:
    def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
        """Initialize a Monster"""
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def is_scary(self):
        """Determine scary monster"""
        return self.number_of_teeth > TEETH or self.colour == COLOUR

    def __str__(self):
        """Display output"""
        return f"{self.name} {self.number_of_teeth} {self.colour} {self.is_scary()} "


monsters = []
monster1 = Monster()
print(monster1)
print(monster1.name)
print(monster1.number_of_teeth)
print(monster1.colour)
print(monster1.is_scary())
monsters.append(monster1)

monster2 = Monster(name="James", number_of_teeth=14, colour="green")
print(monster2)
print(monster2.name)
print(monster2.number_of_teeth)
print(monster2.colour)
print(monster2.is_scary())
monsters.append(monster2)

monster3 = Monster(name="Randall", number_of_teeth=24, colour="purple")
print(monster3)
print(monster3.name)
print(monster3.number_of_teeth)
print(monster3.colour)
print(monster3.is_scary())
monsters.append(monster3)