#Обработка неизвестных команд из API
#Ты получаешь запросы с действиями ({"command": "send_email", "data": {...}}).
# Нужно выполнить разные команды: send_email, export_csv, notify_slack, но список команд может расширяться.
# Паттерны:
# Command — каждая команда инкапсулирует своё поведение
#
# Factory — создаём нужную реализацию по имени
#
# Registry — хранит соответствие имя → класс

class CommandHandler:
    def execute(self, data):
        raise NotImplementedError()

class SendEmail(CommandHandler):
    def execute(self, data):
        print(f"📧 Sending email to {data['to']}")

class ExportCSV(CommandHandler):
    def execute(self, data):
        print(f"💾 Exporting {data['table']} to CSV")

class NotifySlack(CommandHandler):
    def execute(self, data):
        print(f"🔔 Slack notification: {data['message']}")

# Factory + Registry
registry = {
    "send_email": SendEmail,
    "export_csv": ExportCSV,
    "notify_slack": NotifySlack
}

def handle_command(command_dict):
    cmd_name = command_dict["command"]
    cmd_class = registry.get(cmd_name)
    if not cmd_class:
        raise ValueError(f"Unknown command: {cmd_name}")
    handler = cmd_class()
    handler.execute(command_dict["data"])
