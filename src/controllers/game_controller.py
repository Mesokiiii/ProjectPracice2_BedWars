from src.world.game_field import GameField
from src.world.base_building import BaseBuilding
from src.controllers.base_controller import BaseController
from src.controllers.unit_controller import UnitController
from src.utils.property_config import BedWarsProfile
from src.utils.logger import logger


class GameController:
    def __init__(self, width=10, height=10):
        self.field = GameField(width, height, 18)
        self.field.generate_default_world()

        self.base = BaseBuilding("база красных (кровать)", 1, 1, 500, 6)
        self.field.set_base(self.base)

        # создаем двух стартовых бойцов при запуске
        self.base.create_unit("1", self.field)
        self.base.create_unit("3", self.field)

        # задача 4 (вариант 2): класс с декоратором @property и json
        self.profile = BedWarsProfile("Steve", "красная", 100)
        self.saved_field_copy = None

        self.base_controller = BaseController(self.base, self.field)
        self.unit_controller = UnitController(self.base, self.field)
        logger.log("игра запущена")

    def run(self):
        print("\n=== minecraft bedwars: текстовая версия (вариант 2) ===")
        print(self.field.render())

        while True:
            print("\n------------------------------------------------------------")
            print("главное меню |", self.profile.get_text())
            print("------------------------------------------------------------")
            print("1. показать игровое поле")
            print("2. управление базой (создание и учет бойцов)")
            print("3. управление бойцами (перемещение и сбор объектов)")
            print("4. копирование поля (сохранить и восстановить копию поля)")
            print("5. профиль игрока (@property и json - задача 4, вариант 2)")
            print("6. создать новое поле своего размера")
            print("0. выход")

            choice = input("выберите действие: ").strip()
            if choice == "1":
                print(self.field.render())
            elif choice == "2":
                self.base_controller.show_menu()
            elif choice == "3":
                self.unit_controller.show_menu()
            elif choice == "4":
                self.copy_field_menu()
            elif choice == "5":
                self.profile_menu()
            elif choice == "6":
                self.new_size_menu()
            elif choice == "0":
                logger.log("выход из игры")
                print("игра завершена")
                break
            else:
                print("введите цифру от 0 до 6")

    def copy_field_menu(self):
        print("\n--- копирование поля (задача 1) ---")
        print("1. сохранить копию текущего поля")
        print("2. загрузить сохраненную копию поля")
        sub = input("ваш выбор: ").strip()

        if sub == "1":
            self.saved_field_copy = self.field.copy_field()
            print("копия поля успешно сохранена")
        elif sub == "2":
            if self.saved_field_copy is None:
                print("сначала сделайте копию поля (пункт 1)")
            else:
                self.field = self.saved_field_copy.copy_field()
                self.base = self.field.base
                self.base_controller = BaseController(self.base, self.field)
                self.unit_controller = UnitController(self.base, self.field)
                print("поле восстановлено из копии:")
                print(self.field.render())

    def profile_menu(self):
        print("\n--- профиль игрока (@property и json, задача 4) ---")
        print("текущие данные:", self.profile.get_text())
        print("1. изменить ник, цвет команды и изумруды")
        print("2. сохранить в json-файл")
        print("3. загрузить из json-файла")
        sub = input("ваш выбор: ").strip()

        if sub == "1":
            nick = input("введите новый ник: ").strip()
            color = input("введите цвет команды: ").strip()
            ems = input("введите количество изумрудов: ").strip()
            if nick != "":
                self.profile.nickname = nick
            if color != "":
                self.profile.team_color = color
            if ems.isdigit():
                self.profile.emeralds = int(ems)
            print("данные обновлены:", self.profile.get_text())
        elif sub == "2":
            self.profile.save_to_json()
            print("сохранено в файл: saves/bedwars_profile.json")
        elif sub == "3":
            if self.profile.load_from_json():
                print("загружено из файла:", self.profile.get_text())
            else:
                print("файл еще не создан, сначала сохраните профиль")

    def new_size_menu(self):
        w = input("введите ширину поля (например 8): ").strip()
        h = input("введите высоту поля (например 8): ").strip()
        m = input("введите макс. число объектов (например 15): ").strip()

        if w.isdigit() and h.isdigit() and m.isdigit():
            width = max(5, int(w))
            height = max(5, int(h))
            max_obj = max(6, int(m))
            self.field = GameField(width, height, max_obj)
            self.field.generate_default_world()
            self.base = BaseBuilding("база красных (кровать)", 1, 1, 500, 6)
            self.field.set_base(self.base)
            self.base.create_unit("1", self.field)
            self.base_controller = BaseController(self.base, self.field)
            self.unit_controller = UnitController(self.base, self.field)
            print("создано новое поле:")
            print(self.field.render())
        else:
            print("ошибка: нужно вводить числа")
