import copy
import random
from src.world.landscapes import WoolBridgeLandscape, ObsidianPlatformLandscape, VoidGapLandscape
from src.world.neutral_objects import GoldenAppleCrate, DiamondGenerator, EmeraldGenerator, TntTrap
from src.utils.logger import logger


class GameField:
    def __init__(self, width=10, height=10, max_objects=18):
        self.width = width
        self.height = height
        self.max_objects = max_objects

        # создаем двумерный список для ландшафта
        self.grid_landscape = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(WoolBridgeLandscape())
            self.grid_landscape.append(row)

        self.base = None
        self.units = []
        self.neutral_objects = []

    def generate_default_world(self):
        random.seed(42)
        for y in range(self.height):
            for x in range(self.width):
                r = random.random()
                if r < 0.18:
                    self.grid_landscape[y][x] = ObsidianPlatformLandscape()
                elif r < 0.28:
                    self.grid_landscape[y][x] = VoidGapLandscape()
                else:
                    self.grid_landscape[y][x] = WoolBridgeLandscape()

        # добавляем 4 нейтральных объекта
        items = [
            GoldenAppleCrate(3, 2),
            DiamondGenerator(5, 4),
            EmeraldGenerator(2, 6),
            TntTrap(6, 3)
        ]
        for item in items:
            if self.is_inside(item.x, item.y):
                self.grid_landscape[item.y][item.x] = WoolBridgeLandscape()
                self.add_neutral_object(item)

    def total_objects_count(self):
        count = len(self.units) + len(self.neutral_objects)
        if self.base is not None:
            count = count + 1
        return count

    def is_inside(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def set_base(self, base):
        if self.total_objects_count() >= self.max_objects:
            return False
        if not self.is_inside(base.x, base.y):
            return False
        self.grid_landscape[base.y][base.x] = ObsidianPlatformLandscape()
        # делаем клетки вокруг базы проходимыми мостами для спавна
        offsets = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (2, 0), (0, 2)]
        for dx, dy in offsets:
            nx = base.x + dx
            ny = base.y + dy
            if self.is_inside(nx, ny):
                self.grid_landscape[ny][nx] = WoolBridgeLandscape()
        self.base = base
        logger.log(f"база поставлена в точке: ({base.x}, {base.y})")
        return True

    def add_unit(self, unit, x, y):
        if self.total_objects_count() >= self.max_objects:
            return False
        if not self.is_inside(x, y):
            return False
        if self.get_unit_at(x, y) is not None:
            return False
        if not self.grid_landscape[y][x].can_pass(unit):
            return False

        unit.x = x
        unit.y = y
        self.units.append(unit)
        return True

    def remove_unit(self, unit):
        if unit in self.units:
            self.units.remove(unit)
            if unit.base is not None:
                unit.base.on_unit_destroyed(unit)
            logger.log(f"юнит удален с поля: {unit.name}")
            return True
        return False

    def add_neutral_object(self, obj):
        if self.total_objects_count() >= self.max_objects:
            return False
        if not self.is_inside(obj.x, obj.y):
            return False
        self.neutral_objects.append(obj)
        return True

    def remove_neutral_object(self, obj):
        if obj in self.neutral_objects:
            self.neutral_objects.remove(obj)
            return True
        return False

    def get_unit_at(self, x, y):
        for unit in self.units:
            if unit.x == x and unit.y == y:
                return unit
        return None

    def get_neutral_at(self, x, y):
        for obj in self.neutral_objects:
            if obj.x == x and obj.y == y:
                return obj
        return None

    def move_unit(self, unit, new_x, new_y):
        if not self.is_inside(new_x, new_y):
            return False, "ошибка: нельзя выйти за границы карты"

        if self.base is not None and self.base.x == new_x and self.base.y == new_y:
            return False, "ошибка: на этой клетке стоит ваша кровать"

        if self.get_unit_at(new_x, new_y) is not None:
            return False, "ошибка: клетка уже занята другим бойцом"

        landscape = self.grid_landscape[new_y][new_x]
        if not landscape.can_pass(unit):
            return False, f"ошибка: {unit.name} не может пройти через {landscape.name}"

        unit.x = new_x
        unit.y = new_y
        text = landscape.apply_effect(unit)

        # если на клетке есть нейтральный объект, используем перегрузку оператора +
        neutral = self.get_neutral_at(new_x, new_y)
        if neutral is not None and unit.health > 0:
            bonus_text = unit + neutral
            text = text + " | " + bonus_text
            self.remove_neutral_object(neutral)

        if unit.health <= 0:
            self.remove_unit(unit)
            text = text + f" | боец {unit.name} погиб"

        logger.log(text)
        return True, text

    def copy_field(self):
        # глубокое копирование поля вместе со всеми объектами
        logger.log("выполнено копирование игрового поля")
        return copy.deepcopy(self)

    def render(self):
        result = f"\n--- карта bedwars ({self.width}x{self.height}) | объектов на поле: {self.total_objects_count()}/{self.max_objects} ---\n"
        header = "   "
        for x in range(self.width):
            header += f"{x:2d} "
        result += header + "\n"

        for y in range(self.height):
            row_str = f"{y:2d}| "
            for x in range(self.width):
                unit = self.get_unit_at(x, y)
                neutral = self.get_neutral_at(x, y)

                if self.base is not None and self.base.x == x and self.base.y == y:
                    sym = self.base.symbol
                elif unit is not None:
                    sym = unit.symbol
                elif neutral is not None:
                    sym = neutral.symbol
                else:
                    sym = self.grid_landscape[y][x].symbol
                row_str += sym + "  "
            result += row_str + "\n"

        result += "\nобозначения на карте:\n"
        result += "база и бойцы: [B] кровать, [S] мечник, [P] крушитель, [A] лучник, [F] фаербол, [G] голем, [E] эндер\n"
        result += "ландшафт: [.] шерстяной мост, [O] обсидиан (+броня), [~] разлом бездны (-здоровье)\n"
        result += "объекты: [+] золотое яблоко, [D] алмазы, [$] изумруды, [X] динамит"
        return result
