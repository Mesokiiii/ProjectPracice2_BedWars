import os

files_list = [
    "main.py",
    "task4_variant2.py",
    "src/interfaces/base_interfaces.py",
    "src/units/base_unit.py",
    "src/units/infantry.py",
    "src/units/archers.py",
    "src/units/cavalry.py",
    "src/world/landscapes.py",
    "src/world/neutral_objects.py",
    "src/world/base_building.py",
    "src/world/game_field.py",
    "src/controllers/base_controller.py",
    "src/controllers/unit_controller.py",
    "src/controllers/game_controller.py",
    "src/utils/logger.py",
    "src/utils/property_config.py"
]

out = open("all_code.txt", "w", encoding="utf-8")

for path in files_list:
    if os.path.exists(path):
        out.write("========================================\n")
        out.write(f"файл: {path}\n")
        out.write("========================================\n\n")

        f = open(path, "r", encoding="utf-8")
        content = f.read()
        f.close()

        out.write(content + "\n\n")

out.close()
print("весь код успешно собран в файл: all_code.txt")
