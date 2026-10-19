class UnitController:
    def __init__(self, base, field):
        self.base = base
        self.field = field

    def show_menu(self):
        if len(self.base.units) == 0:
            print("\nна поле нет бойцов, сначала создайте их на базе")
            return

        while True:
            print("\n--- выбор бойца для управления ---")
            for i in range(len(self.base.units)):
                print(f"{i + 1}. {self.base.units[i].get_info()}")
            print("0. назад в главное меню")

            choice = input("введите номер бойца: ").strip()
            if choice == "0":
                break

            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(self.base.units):
                    self.control_unit(self.base.units[idx])
                else:
                    print("нет бойца с таким номером")
            else:
                print("введите цифру")

    def control_unit(self, unit):
        while unit in self.base.units:
            print(self.field.render())
            print("\nвыбранный боец:", unit.get_info())
            print("управление: [w] вверх | [s] вниз | [a] влево | [d] вправо | [i] подобрать объект | [0] назад")
            cmd = input("ваш ход: ").strip().lower()

            if cmd == "0":
                break
            elif cmd == "w":
                ok, text = unit.move(0, -1, self.field)
                print("результат:", text)
            elif cmd == "s":
                ok, text = unit.move(0, 1, self.field)
                print("результат:", text)
            elif cmd == "a":
                ok, text = unit.move(-1, 0, self.field)
                print("результат:", text)
            elif cmd == "d":
                ok, text = unit.move(1, 0, self.field)
                print("результат:", text)
            elif cmd == "i":
                obj = self.field.get_neutral_at(unit.x, unit.y)
                if obj is not None:
                    # перегрузка оператора +
                    print("взаимодействие:", unit + obj)
                    self.field.remove_neutral_object(obj)
                    if unit.health <= 0:
                        self.field.remove_unit(unit)
                        print("боец погиб")
                        break
                else:
                    print("на этой клетке нет нейтрального объекта")
            else:
                print("неизвестная команда")
