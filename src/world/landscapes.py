from src.interfaces.base_interfaces import ILandscape


class BaseLandscape(ILandscape):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def can_pass(self, unit):
        return True

    def apply_effect(self, unit):
        return f"юнит {unit.name} встал на блок: {self.name}"


class WoolBridgeLandscape(BaseLandscape):
    # тип 1: шерстяной мост
    def __init__(self):
        super().__init__("шерстяной мост", ".")

    def apply_effect(self, unit):
        return f"{unit.name} пробежал по шерстяному мосту"


class ObsidianPlatformLandscape(BaseLandscape):
    # тип 2: обсидиановая платформа
    def __init__(self):
        super().__init__("обсидиан", "O")

    def apply_effect(self, unit):
        unit.armor = unit.armor + 3
        return f"обсидиан укрепил защиту {unit.name}: +3 к броне"


class VoidGapLandscape(BaseLandscape):
    # тип 3: разлом бездны
    def __init__(self):
        super().__init__("разлом бездны", "~")

    def can_pass(self, unit):
        if unit.name == "железный голем":
            return False
        return True

    def apply_effect(self, unit):
        unit.take_damage(8)
        return f"{unit.name} перепрыгнул разлом бездны и потерял немного здоровья"
