class BaseController:
    def __init__(self, base, field):
        self.base = base
        self.field = field

    def show_menu(self):
        while True:
            print("\n--- управление базой (кроватью) ---")
            print("1. показать состояние базы и список бойцов")
            print("2. создать нового бойца")
            print("3. удалить бойца с поля")
            print("4. удалить нейтральный объект с поля")
            print("0. назад в главное меню")

            choice = input("выберите пункт: ").strip()
            if choice == "1":
                print("\n" + self.base.get_status())
            elif choice == "2":
                self.recruit_unit()
            elif choice == "3":
                self.remove_unit()
            elif choice == "4":
                self.remove_neutral()
            elif choice == "0":
                break
            else:
                print("неверный ввод, попробуйте еще раз")

    def recruit_unit(self):
        print("\nкого создать возле кровати:")
        print("1. алмазный мечник (тип: рашеры)")
        print("2. крушитель кроватей (тип: рашеры)")
        print("3. лучник-снайпер (тип: снайперы)")
        print("4. метатель фаерболов (тип: снайперы)")
        print("5. железный голем (тип: мобы-защитники)")
        print("6. эндер-рашер (тип: мобы-защитники)")

        code = input("введите номер бойца (1-6): ").strip()
        ok, text = self.base.create_unit(code, self.field)
        print(text)

    def remove_unit(self):
        if len(self.base.units) == 0:
            print("у базы сейчас нет бойцов")
            return

        print("\nсписок бойцов:")
        for i in range(len(self.base.units)):
            print(f"{i + 1}. {self.base.units[i].get_info()}")

        num = input("введите номер бойца для удаления: ").strip()
        if num.isdigit():
            idx = int(num) - 1
            if 0 <= idx < len(self.base.units):
                unit = self.base.units[idx]
                self.field.remove_unit(unit)
                print(f"боец удален: {unit.name}")
            else:
                print("неверный номер")
        else:
            print("нужно ввести число")

    def remove_neutral(self):
        if len(self.field.neutral_objects) == 0:
            print("на поле больше нет нейтральных объектов")
            return

        print("\nсписок нейтральных объектов на поле:")
        for i in range(len(self.field.neutral_objects)):
            obj = self.field.neutral_objects[i]
            print(f"{i + 1}. [{obj.symbol}] {obj.name} на клетке ({obj.x}, {obj.y})")

        num = input("введите номер объекта для удаления: ").strip()
        if num.isdigit():
            idx = int(num) - 1
            if 0 <= idx < len(self.field.neutral_objects):
                obj = self.field.neutral_objects[idx]
                self.field.remove_neutral_object(obj)
                print(f"объект удален с поля: {obj.name}")
            else:
                print("неверный номер")
        else:
            print("нужно ввести число")
