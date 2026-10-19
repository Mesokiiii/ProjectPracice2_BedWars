from src.interfaces.base_interfaces import INeutralObject


class BaseNeutralObject(INeutralObject):
    def __init__(self, name, symbol, x=0, y=0):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y

    def interact(self, unit):
        return f"{unit.name} подобрал {self.name}"

    def __radd__(self, unit):
        return self.interact(unit)


class GoldenAppleCrate(BaseNeutralObject):
    # объект 1: золотое яблоко
    def __init__(self, x=0, y=0):
        super().__init__("золотое яблоко", "+", x, y)

    def interact(self, unit):
        unit.health = unit.health + 30
        return f"золотое яблоко: {unit.name} получил +30 к здоровью (теперь: {unit.health})"


class DiamondGenerator(BaseNeutralObject):
    # объект 2: алмазный генератор
    def __init__(self, x=0, y=0):
        super().__init__("алмазный генератор", "D", x, y)

    def interact(self, unit):
        unit.armor = unit.armor + 12
        return f"алмазный генератор: {unit.name} прокачал броню на +12 (теперь: {unit.armor})"


class EmeraldGenerator(BaseNeutralObject):
    # объект 3: изумрудный генератор
    def __init__(self, x=0, y=0):
        super().__init__("изумрудный генератор", "$", x, y)

    def interact(self, unit):
        unit.attack = unit.attack + 15
        return f"изумрудный генератор: {unit.name} прокачал атаку на +15 (теперь: {unit.attack})"


class TntTrap(BaseNeutralObject):
    # объект 4: ловушка с динамитом
    def __init__(self, x=0, y=0):
        super().__init__("динамит tnt", "X", x, y)

    def interact(self, unit):
        unit.take_damage(25)
        return f"динамит tnt взорвался: {unit.name} получил урон (осталось здоровья: {unit.health})"
