from src.units.base_unit import BaseUnit


class SniperUnit(BaseUnit):
    # тип 2: снайперы (дальний бой)
    def __init__(self, name, health, armor, attack, symbol, x=0, y=0, base=None):
        super().__init__(name, "снайперы", health, armor, attack, symbol, x, y, base)


class BowSpammer(SniperUnit):
    # вид 1: лучник-снайпер
    def __init__(self, x=0, y=0, base=None):
        super().__init__("лучник-снайпер", 70, 10, 38, "A", x, y, base)


class FireballThrower(SniperUnit):
    # вид 2: метатель фаерболов
    def __init__(self, x=0, y=0, base=None):
        super().__init__("метатель фаерболов", 75, 12, 48, "F", x, y, base)
