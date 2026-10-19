import json


class BedWarsProfile:
    def __init__(self, nickname="Steve", team_color="красная", emeralds=100):
        self._nickname = nickname
        self._team_color = team_color
        self._emeralds = emeralds

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        if value != "":
            self._nickname = value

    @property
    def team_color(self):
        return self._team_color

    @team_color.setter
    def team_color(self, value):
        if value != "":
            self._team_color = value

    @property
    def emeralds(self):
        return self._emeralds

    @emeralds.setter
    def emeralds(self, value):
        if value >= 0:
            self._emeralds = value
        else:
            self._emeralds = 0

    def save_to_json(self, filename="saves/bedwars_profile.json"):
        # сохраняем сам объект и информацию о классе в json
        data = {
            "class_name": self.__class__.__name__,
            "attributes": ["nickname", "team_color", "emeralds"],
            "nickname": self._nickname,
            "team_color": self._team_color,
            "emeralds": self._emeralds
        }
        file = open(filename, "w", encoding="utf-8")
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.close()

    def load_from_json(self, filename="saves/bedwars_profile.json"):
        try:
            file = open(filename, "r", encoding="utf-8")
            data = json.load(file)
            file.close()
            self.nickname = data["nickname"]
            self.team_color = data["team_color"]
            self.emeralds = data["emeralds"]
            return True
        except:
            return False

    def get_text(self):
        return f"игрок: {self.nickname} | команда: {self.team_color} | изумруды: {self.emeralds}"
