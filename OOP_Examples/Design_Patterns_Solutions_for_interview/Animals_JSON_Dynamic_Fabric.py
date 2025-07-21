#Получаем на вход JSON file в котором приходят любые животные, их цвет и голос

# Паттерн	Назначение
# Factory	Создание объектов без знания конкретных классов
# Registry	Кэширование классов по имени (_registry)
# Dynamic Class Generation	type(name, bases, dict) для создания классов «на лету»
# Duck Typing	Мы не зависим от типа, только от интерфейса (speak())

import json

# Наши «животные» умеют говорить
class Animal:
    def __init__(self, color, sound):
        self.color = color
        self.sound = sound

    def speak(self):
        return f"{self.__class__.__name__} says {self.sound}"

    def describe(self):
        return f"A {self.color} {self.__class__.__name__}"

# Фабрика, создающая классы динамически
class AnimalFactory:
    _registry = {}

    @classmethod
    def create_animal(cls, type_name, color, sound):
        # Если класс ещё не зарегистрирован — создаём на лету
        if type_name not in cls._registry:
            # Создаём новый подкласс Animal с нужным именем
            new_class = type(type_name.capitalize(), (Animal,), {})
            cls._registry[type_name] = new_class

        # Возвращаем экземпляр
        return cls._registry[type_name](color, sound)

# Пример JSON
data = json.loads('''[
    {"type": "cat", "color": "white", "sound": "meow"},
    {"type": "dog", "color": "brown", "sound": "woof"},
    {"type": "unicorn", "color": "rainbow", "sound": "sparkle"},
    {"type": "robot_sheep", "color": "metal", "sound": "beep"}
]''')

animals = []

# Использование
for entry in data:
    animals.append(AnimalFactory.create_animal(entry["type"], entry["color"], entry["sound"]))

for animal in animals:
    print(animal.describe())
    print(animal.speak())

