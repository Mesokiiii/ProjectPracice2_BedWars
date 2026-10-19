from src.units.base_unit import BaseUnit


class RusherUnit(BaseUnit):
    # тип 1: рашеры (ближний бой)
    def __init__(self, name, health, armor, attack, symbol, x=0, y=0, base=None):
        super().__init__(name, "рашеры", health, armor, attack, symbol, x, y, base)


class SwordRusher(RusherUnit):
    # вид 1: алмазный мечник
    def __init__(self, x=0, y=0, base=None):
        super().__init__("алмазный мечник", 100, 20, 30, "S", x, y, base)


class BedBreaker(RusherUnit):
    # вид 2: крушитель кроватей
    def __init__(self, x=0, y=0, base=None):
        super().__init__("крушитель кроватей", 90, 15, 40, "P", x, y, base)
