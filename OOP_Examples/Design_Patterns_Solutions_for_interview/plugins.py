# ЗАДАЧА 4: 🔌 Плагины для тестовой платформы
# 📌 Описание:
# У тебя есть тестовая система. Ты хочешь, чтобы можно было подключать внешние плагины — например, экспорт в Excel,
# интеграция с TestRail и т.п., не меняя основной код.
# Паттерны:
# Plugin / Registry — позволяет динамически подключать функциональность
# Decorator (метапрограммирование) — регистрирует классы как плагины

plugin_registry = {}

def register_plugin(name):
    def decorator(cls):
        plugin_registry[name] = cls()
        return cls
    return decorator

@register_plugin("testrail")
class TestRailPlugin:
    def run(self, test_data):
        print("Exporting to TestRail")

@register_plugin("excel")
class ExcelPlugin:
    def run(self, test_data):
        print("Saving to Excel")

def run_plugin(name, data):
    plugin = plugin_registry[name]
    plugin.run(data)
