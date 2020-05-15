class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Food(Item):
    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.health = health

    def eat(self, food):
        pass


class Tool(Item):
    def __init__(self, name, description, action):
        super().__init__(name, description)
        self.action = action

    def use(self, tool):
        pass


class Trap(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def trip(self, trap):
        pass
