# Задача 5: Команда-обработчик (Command + Factory)
# Паттерны:
# Command — команды как объекты.
#
# Factory — генерация команды по имени.
#
# Registry — хранение доступных команд.

import json
class Command:
    def execute(self):
        raise NotImplementedError

class CommandRegistry:
    _map = {}

    @classmethod
    def register(cls, name):
        def wrapper(c):
            cls._map[name] = c
            return c
        return wrapper

    @classmethod
    def get(cls, name):
        if name not in cls._map:
            raise Exception(f"Unknown command: {name}")
        return cls._map[name]()

@CommandRegistry.register("restart_server")
class RestartServer(Command):
    def execute(self):
        print("Restarting server...")

@CommandRegistry.register("clear_cache")
class ClearCache(Command):
    def execute(self):
        print("Clearing cache...")

@CommandRegistry.register("notify_admin")
class NotifyAdmin(Command):
    def execute(self):
        print("Sending admin notification...")

cmds = json.loads('''[
  {"command": "restart_server"},
  {"command": "clear_cache"},
  {"command": "notify_admin"}
]''')

for cmd in cmds:
    c = CommandRegistry.get(cmd["command"])
    c.execute()
