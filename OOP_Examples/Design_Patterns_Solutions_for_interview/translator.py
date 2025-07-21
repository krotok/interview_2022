# ✅ Задача 4: Многоязычный переводчик из JSON (Strategy + Registry)
# Паттерны:
# Strategy — переводчик как стратегия обработки текста.
#
# Factory + Registry — динамический выбор переводчика.

import json

class Translator:
    def translate(self, text):
        raise NotImplementedError

class TranslatorRegistry:
    _map = {}

    @classmethod
    def register(cls, lang):
        def decorator(c):
            cls._map[lang] = c
            return c
        return decorator

    @classmethod
    def get(cls, lang):
        if lang not in cls._map:
            raise ValueError(f"Unsupported language: {lang}")
        return cls._map[lang]()

@TranslatorRegistry.register("en")
class EnglishTranslator(Translator):
    def translate(self, text):
        return f"EN: {text}"

@TranslatorRegistry.register("es")
class SpanishTranslator(Translator):
    def translate(self, text):
        return f"ES: {text}"

@TranslatorRegistry.register("fr")
class FrenchTranslator(Translator):
    def translate(self, text):
        return f"FR: {text}"

data = json.loads('''[
  {"lang": "en", "text": "Hello"},
  {"lang": "es", "text": "Hola"},
  {"lang": "fr", "text": "Bonjour"}
]''')

for item in data:
    t = TranslatorRegistry.get(item["lang"])
    print(t.translate(item["text"]))
