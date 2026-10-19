from src.units.base_unit import BaseUnit


class MobsUnit(BaseUnit):
    # тип 3: мобы-защитники
    def __init__(self, name, health, armor, attack, symbol, x=0, y=0, base=None):
        super().__init__(name, "мобы-защитники", health, armor, attack, symbol, x, y, base)


class IronGolem(MobsUnit):
    # вид 1: железный голем
    def __init__(self, x=0, y=0, base=None):
        super().__init__("железный голем", 150, 35, 35, "G", x, y, base)


class EnderRider(MobsUnit):
    # вид 2: эндер-рашер
    def __init__(self, x=0, y=0, base=None):
        super().__init__("эндер-рашер", 110, 22, 45, "E", x, y, base)
