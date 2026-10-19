import os
from src.utils.property_config import BedWarsProfile


if not os.path.exists("saves"):
    os.mkdir("saves")

print("--- проверка задачи 4 (вариант 2) ---")

profile = BedWarsProfile("Dream", "зеленая", 250)
print("создан профиль:", profile.get_text())

profile.nickname = "Technoblade"
profile.emeralds = 500
print("после изменения через @property:", profile.get_text())

profile.save_to_json("saves/task4_bedwars.json")
print("сохранено в файл: saves/task4_bedwars.json")

new_profile = BedWarsProfile()
new_profile.load_from_json("saves/task4_bedwars.json")
print("загружено из файла:", new_profile.get_text())
