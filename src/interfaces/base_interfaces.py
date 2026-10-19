class IUnit:
    # общий интерфейс для юнитов
    def move(self, dx, dy, field):
        pass

    def get_info(self):
        pass


class ILandscape:
    # общий интерфейс для ландшафта
    def can_pass(self, unit):
        pass

    def apply_effect(self, unit):
        pass


class INeutralObject:
    # общий интерфейс для нейтральных объектов
    def interact(self, unit):
        pass
