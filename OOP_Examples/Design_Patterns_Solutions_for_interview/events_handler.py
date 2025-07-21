#  Задача 1: Динамическая обработка событий из JSON (Observer + Factory)
# Описание:
# У нас есть JSON с событиями, которые должны вызывать разные обработчики (уведомления по email, логгирование, отправка в Slack и т.д.).
#  Типы событий заранее неизвестны.
# Паттерны:
# Observer — каждое событие вызывает соответствующего слушателя (handle).
# Factory — get_handler() создает обработчик по типу.
# Registry — хранит мапу event_type -> handler class

# Базовый интерфейс для всех обработчиков событий
class EventHandler:
    def handle(self, message):
        raise NotImplementedError

# Фабрика + Observer регистрация
class EventRegistry:
    _handlers = {}

    @classmethod
    def register(cls, event_type):
        def decorator(handler_cls):
            cls._handlers[event_type] = handler_cls
            return handler_cls
        return decorator

    @classmethod
    def get_handler(cls, event_type):
        handler_cls = cls._handlers.get(event_type)
        if not handler_cls:
            raise ValueError(f"Unknown event type: {event_type}")
        return handler_cls()

# Обработчики (наблюдатели)
@EventRegistry.register("email")
class EmailHandler(EventHandler):
    def handle(self, message):
        print(f"[EMAIL] {message}")

@EventRegistry.register("slack")
class SlackHandler(EventHandler):
    def handle(self, message):
        print(f"[SLACK] {message}")

@EventRegistry.register("sms")
class SMSHandler(EventHandler):
    def handle(self, message):
        print(f"[SMS] {message}")

# Имитация входящих событий
import json

events = json.loads('''[
    {"type": "email", "message": "Server down"},
    {"type": "slack", "message": "Deployment done"},
    {"type": "sms", "message": "User signed up"}
]''')

# Обработка
for event in events:
    handler = EventRegistry.get_handler(event["type"])
    handler.handle(event["message"])
