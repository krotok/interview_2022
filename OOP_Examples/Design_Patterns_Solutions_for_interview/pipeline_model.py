# ЗАДАЧА 5: 🧪 Моделирование тестовых шагов как pipeline
# 📌 Описание:
# Тест состоит из шагов: авторизация, отправка запроса, проверка результата. Нужно уметь строить пайплайн, где шаги можно переиспользовать и менять порядок.
# Паттерны:
# Chain of Responsibility — шаги обрабатываются последовательно
# Strategy — поведение шага изолировано
# Template Method (если нужно общее поведение и абстрактные шаги)

class Step:
    def run(self, context):
        raise NotImplementedError()

class AuthStep(Step):
    def run(self, context):
        context["token"] = "123abc"

class RequestStep(Step):
    def run(self, context):
        print("Sending request with token", context["token"])

class AssertStep(Step):
    def run(self, context):
        print("Asserting results...")

scenario = [AuthStep(), RequestStep(), AssertStep()]
context = {}

for step in scenario:
    step.run(context)
