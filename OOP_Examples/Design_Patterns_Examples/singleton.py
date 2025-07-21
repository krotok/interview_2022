#Юс кейсы
#1. Гловальный логер
#2. Подключение к базе данных
#3. Создание кеша

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

config1 = Singleton()
config2 = Singleton()
print(f"{id(config1)} {id(config2)}")
print(config1 is config2)  # True
