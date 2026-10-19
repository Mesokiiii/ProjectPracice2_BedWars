from src.units.infantry import SwordRusher, BedBreaker
from src.units.archers import BowSpammer, FireballThrower
from src.units.cavalry import IronGolem, EnderRider
from src.utils.logger import logger


class BaseBuilding:
    def __init__(self, name="база красных (кровать)", x=1, y=1, health=500, max_units=6):
        self.name = name
        self.x = x
        self.y = y
        self.health = health
        self.max_units = max_units
        self.symbol = "B"
        self.units = []

    def create_unit(self, choice, field):
        if len(self.units) >= self.max_units:
            return False, f"ошибка: на базе уже максимум бойцов ({self.max_units})"

        spawn_pos = self.find_free_place(field)
        if spawn_pos is None:
            return False, "ошибка: вокруг кровати нет свободных клеток"

        sx = spawn_pos[0]
        sy = spawn_pos[1]

        if choice == "1":
            new_unit = SwordRusher(sx, sy, self)
        elif choice == "2":
            new_unit = BedBreaker(sx, sy, self)
        elif choice == "3":
            new_unit = BowSpammer(sx, sy, self)
        elif choice == "4":
            new_unit = FireballThrower(sx, sy, self)
        elif choice == "5":
            new_unit = IronGolem(sx, sy, self)
        elif choice == "6":
            new_unit = EnderRider(sx, sy, self)
        else:
            return False, "ошибка: неверный номер бойца"

        added = field.add_unit(new_unit, sx, sy)
        if added:
            self.units.append(new_unit)
            msg = f"создан юнит: {new_unit.name} на клетке ({sx}, {sy})"
            logger.log(msg)
            return True, msg
        else:
            return False, "ошибка: не удалось поставить юнита на поле"

    def find_free_place(self, field):
        steps = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (2, 0), (0, 2)]
        for dx, dy in steps:
            nx = self.x + dx
            ny = self.y + dy
            if field.is_inside(nx, ny):
                if field.get_unit_at(nx, ny) is None:
                    if not (nx == self.x and ny == self.y):
                        return (nx, ny)
        return None

    def on_unit_destroyed(self, unit):
        if unit in self.units:
            self.units.remove(unit)
            logger.log(f"база зафиксировала гибель юнита: {unit.name}")

    def get_status(self):
        text = f"--- состояние базы: {self.name} ---\n"
        text += f"координаты кровати: ({self.x}, {self.y})\n"
        text += f"прочность кровати: {self.health}\n"
        text += f"количество юнитов: {len(self.units)} из {self.max_units}\n"

        if len(self.units) == 0:
            text += "список юнитов: пусто"
        else:
            text += "список юнитов:\n"
            for i in range(len(self.units)):
                text += f"  {i + 1}. {self.units[i].get_info()}\n"
        return text
