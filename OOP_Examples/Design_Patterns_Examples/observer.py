#нужен когда требуется одновременно обратиться ко всем классам
#1. отослать сообщение по мейлу в слек и записать в лог
#2. Записть сообщение в лог и выдать на экран

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, msg):
        for o in self._observers:
            o.update(msg)

class Observer:
    def update(self, msg):
        print(f"Received: {msg}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()
subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")


############################## Make Observer for Notifications ##########################
# NotificationChannel	Интерфейс наблюдателя
# EmailNotifier, SlackNotifier, SMSNotifier	Реализация наблюдателей
# NotificationManager	Хранит список наблюдателей и вызывает их

from abc import ABC, abstractmethod

# ---------- Observer (абстрактный наблюдатель) ----------
class NotificationChannel(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass


# ---------- Concrete Observers ----------
class EmailNotifier(NotificationChannel):
    def notify(self, message: str):
        print(f"📧 Email: {message}")


class SlackNotifier(NotificationChannel):
    def notify(self, message: str):
        print(f"💬 Slack: {message}")


class SMSNotifier(NotificationChannel):
    def notify(self, message: str):
        print(f"📱 SMS: {message}")


# ---------- Subject (издатель) ----------
class NotificationManager:
    def __init__(self):
        self._observers: list[NotificationChannel] = []

    def subscribe(self, observer: NotificationChannel):
        self._observers.append(observer)

    def unsubscribe(self, observer: NotificationChannel):
        self._observers.remove(observer)

    def notify_all(self, message: str):
        print("🔔 Sending notification to all channels...")
        for observer in self._observers:
            observer.notify(message)


# ---------- Использование ----------
if __name__ == "__main__":
    manager = NotificationManager()

    # Подписываем каналы
    manager.subscribe(EmailNotifier())
    manager.subscribe(SlackNotifier())
    manager.subscribe(SMSNotifier())

    # Событие, вызывающее уведомление
    manager.notify_all("Build failed on Jenkins job #42 ❌")
