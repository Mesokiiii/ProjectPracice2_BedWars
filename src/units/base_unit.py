from src.interfaces.base_interfaces import IUnit, INeutralObject
from src.utils.logger import logger


class BaseUnit(IUnit):
    def __init__(self, name, unit_type, health, armor, attack, symbol, x=0, y=0, base=None):
        self.name = name
        self.unit_type = unit_type
        self.health = health
        self.armor = armor
        self.attack = attack
        self.symbol = symbol
        self.x = x
        self.y = y
        self.base = base

    def move(self, dx, dy, field):
        new_x = self.x + dx
        new_y = self.y + dy
        return field.move_unit(self, new_x, new_y)

    def take_damage(self, damage):
        real_damage = damage - (self.armor // 4)
        if real_damage < 1:
            real_damage = 1
        self.health = self.health - real_damage
        logger.log(f"юнит {self.name} получил урон: {real_damage}")

        if self.health <= 0:
            self.health = 0
            if self.base is not None:
                self.base.on_unit_destroyed(self)

    def get_info(self):
        return f"[{self.symbol}] {self.name} (тип: {self.unit_type}) | здоровье: {self.health}, броня: {self.armor}, атака: {self.attack} | координаты: ({self.x}, {self.y})"

    def __add__(self, other):
        # перегрузка оператора + для взаимодействия с нейтральным объектом
        if isinstance(other, INeutralObject):
            result = other.interact(self)
            logger.log(f"взаимодействие: {result}")
            return result
        return "нельзя сложить эти объекты"
