# Minecraft BedWars: текстовая версия (практическая работа №2)

## Информация по работе
- **вариант выполнения:** вариант 2
- **сложность выполнения задания:** well-done (выполнены все задачи 1–4, задача 4 решена отдельно в `task4_variant2.py` и добавлена в игру, пишутся логи в `logs/game.log`, поле выводится сразу после запуска)
- **список выполненных задач:**
  1. **задача 1 (основные классы):**
     - класс игрового поля `GameField` (`src/world/game_field.py`): создание поля любого размера, контроль максимума объектов, добавление и удаление объектов, копирование поля вместе с объектами (`copy_field`).
     - классы юнитов с общим интерфейсом `IUnit` (`src/interfaces/base_interfaces.py`), 3 типа и по 2 вида в каждом:
       - **тип 1 (рашеры):** `SwordRusher` (алмазный мечник), `BedBreaker` (крушитель кроватей)
       - **тип 2 (снайперы):** `BowSpammer` (лучник-снайпер), `FireballThrower` (метатель фаерболов)
       - **тип 3 (мобы-защитники):** `IronGolem` (железный голем), `EnderRider` (эндер-рашер)
  2. **задача 2 (интерфейсы, взаимодействие классов, перегрузка операций):**
     - класс базы `BaseBuilding` (`src/world/base_building.py`): кровать на поле `[B]`, создание юнитов, учет количества и реакция на их уничтожение (`on_unit_destroyed`).
     - 3 типа ландшафта с общим интерфейсом `ILandscape` (`src/world/landscapes.py`):
       - `WoolBridgeLandscape` (`.`) — шерстяной мост
       - `ObsidianPlatformLandscape` (`O`) — обсидиан (+3 к броне)
       - `VoidGapLandscape` (`~`) — разлом бездны (непроходим для железного голема, остальным снимает здоровье)
     - 4 типа нейтральных объектов с общим интерфейсом `INeutralObject` и перегрузкой операции `+` (`unit + neutral_obj`) (`src/world/neutral_objects.py`):
       - `GoldenAppleCrate` (`+`) — золотое яблоко (+30 здоровья)
       - `DiamondGenerator` (`D`) — алмазный генератор (+12 брони)
       - `EmeraldGenerator` (`$`) — изумрудный генератор (+15 атаки)
       - `TntTrap` (`X`) — динамит tnt (-25 здоровья)
  3. **задача 3 (взаимодействие пользователя с игрой):**
     - управление базой и бойцами через консольное меню (`src/controllers/`).
  4. **задача 4 (вариант 2 — `@property` и json):**
     - класс `BedWarsProfile` (`src/utils/property_config.py`): доступ к переменным через декоратор `@property`, сохранение и загрузка в json-файл (`saves/bedwars_profile.json`).

## Структура папок
```text
Project/
├── main.py                      # запуск игры
├── task4_variant2.py            # отдельное решение задачи 4 (вариант 2)
├── README.md                    # описание проекта
├── repo_link.txt                # ссылка на репозиторий
├── docs/
│   └── class_diagram.drawio     # диаграмма классов в draw.io
├── logs/
│   └── game.log                 # файл логов
├── saves/
│   └── bedwars_profile.json     # сохранение профиля в json
└── src/
    ├── interfaces/
    │   └── base_interfaces.py
    ├── units/
    │   ├── base_unit.py
    │   ├── infantry.py
    │   ├── archers.py
    │   └── cavalry.py
    ├── world/
    │   ├── game_field.py
    │   ├── base_building.py
    │   ├── landscapes.py
    │   └── neutral_objects.py
    ├── controllers/
    │   ├── game_controller.py
    │   ├── base_controller.py
    │   └── unit_controller.py
    └── utils/
        ├── logger.py
        └── property_config.py
```

## Версия python и библиотек
- **python:** 3.10+ (используются только встроенные модули `os`, `json`, `copy`, `random`).

## Инструкции по запуску
1. запуск основной игры:
   ```bash
   python main.py
   ```
2. запуск отдельного файла по задаче 4:
   ```bash
   python task4_variant2.py
   ```

## Краткая справка
- после запуска `python main.py` сразу отображается карта `10x10` и главное меню
- пункт `2` управляет кроватью (базой): просмотр состояния, создание и удаление бойцов
- пункт `3` управляет выбранным бойцом: шаг на `w`, `a`, `s`, `d` и подбор объекта на `i`
- пункт `4` делает копию всего поля и восстанавливает его
- пункт `5` изменяет профиль через `@property` и сохраняет/загружает его в json
