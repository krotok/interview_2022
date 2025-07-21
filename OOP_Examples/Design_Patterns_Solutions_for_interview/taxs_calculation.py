# Задача 2: Плагинная система расчёта налога (Strategy + Factory)
# Паттерны:
# Strategy — разные стратегии налогообложения.
#
# Factory — выбор стратегии по региону.
#
# Registry — для регистрации стратегий.

class TaxStrategy:
    def calculate(self, amount):
        raise NotImplementedError

class TaxFactory:
    _strategies = {}

    @classmethod
    def register(cls, region):
        def decorator(cls_):
            cls._strategies[region] = cls_
            return cls_
        return decorator

    @classmethod
    def get_strategy(cls, region):
        strategy = cls._strategies.get(region)
        if not strategy:
            raise ValueError(f"Unknown region: {region}")
        return strategy()

@TaxFactory.register("EU")
class EUTax(TaxStrategy):
    def calculate(self, amount):
        return amount * 0.2

@TaxFactory.register("US")
class USTax(TaxStrategy):
    def calculate(self, amount):
        return amount * 0.1

@TaxFactory.register("IN")
class IndiaTax(TaxStrategy):
    def calculate(self, amount):
        return amount * 0.18

import json

orders = json.loads('''[
    {"region": "EU", "amount": 100},
    {"region": "US", "amount": 200},
    {"region": "IN", "amount": 300}
]''')

for order in orders:
    strategy = TaxFactory.get_strategy(order["region"])
    tax = strategy.calculate(order["amount"])
    print(f"{order['region']} tax: {tax}")


