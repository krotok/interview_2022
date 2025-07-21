# ✅ Задача 3: Рендеринг UI-компонентов по JSON (Factory + Composite)
# Паттерны:
# Factory — UIComponentFactory.create(...)
#
# Composite (опционально) — можно сгруппировать компоненты в layout.

class UIComponent:
    def render(self):
        raise NotImplementedError

class UIComponentFactory:
    _registry = {}

    @classmethod
    def register(cls, name):
        def decorator(c):
            cls._registry[name] = c
            return c
        return decorator

    @classmethod
    def create(cls, type_name, **kwargs):
        component_cls = cls._registry.get(type_name)
        if not component_cls:
            raise ValueError(f"Unknown UI component: {type_name}")
        return component_cls(**kwargs)

@UIComponentFactory.register("button")
class Button(UIComponent):
    def __init__(self, label):
        self.label = label
    def render(self):
        return f"<button>{self.label}</button>"

@UIComponentFactory.register("input")
class Input(UIComponent):
    def __init__(self, placeholder):
        self.placeholder = placeholder
    def render(self):
        return f"<input placeholder='{self.placeholder}' />"

@UIComponentFactory.register("checkbox")
class Checkbox(UIComponent):
    def __init__(self, checked):
        self.checked = checked
    def render(self):
        return f"<input type='checkbox' {'checked' if self.checked else ''} />"

import json
components = json.loads('''[
  {"type": "button", "label": "Submit"},
  {"type": "input", "placeholder": "Enter name"},
  {"type": "checkbox", "checked": true}
]''')

for comp in components:
    instance = UIComponentFactory.create(comp["type"], **{k: v for k, v in comp.items() if k != "type"})
    print(instance.render())
