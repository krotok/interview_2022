# 📁 project_root/

# ─────────────────────────────────────────────────────────
# 📄 README.md

# 🔧 Automation & Load Testing Framework

Этот проект объединяет API-тестирование, мок-сервер, нагрузочное тестирование через JMeter и визуализацию через Grafana. Всё это интегрировано в Jenkins CI.

## 📁 Структура проекта
```
project_root/
├── src/                   # Основная бизнес-логика и паттерны
├── tests/                 # Pytest + Allure тесты
├── mock/                  # Flask-мок сервер
├── jmeter/                # JMeter тест-план
├── grafana/               # Grafana дашборды
├── Jenkinsfile            # CI pipeline
├── requirements.txt       # Python зависимости
├── README.md              # Документация
└── conftest.py            # Фикстуры для Pytest
```
```project_root/
├── src/
│   ├── client.py ***API-клиент
│   ├── config.py ***Singleton для конфигурации
│   ├── request_factory.py ***Factory: генерация конкретных запросов
│   ├── builder.py ***Builder: пошаговая сборка HTTP-запроса
│   ├── auth_strategy.py ***Strategy: TokenAuth и NoAuth
│   └── logger_util.py ***логгер, подключён ко всем модулям
├── tests/
│   └── test_users.py ***два Allure-теста GET и POST
├── mock/
│   └── mock_server.py ***Flask-мок API /users/{id}, /users
├── jmeter/
│   └── test_plan.jmx ***# Дашборд метрик из InfluxDB
├── Jenkinsfile
├── requirements.txt
└── README.md
```

## 🚀 Запуск локально
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск мок-сервера
python mock/mock_server.py

# Запуск тестов
pytest tests/ --alluredir=allure-results

# Генерация отчета Allure (при установленном allure CLI)
allure serve allure-results
```

## ⚙️ Запуск в Jenkins
CI-процесс в Jenkins включает:
1. Установку зависимостей
2. Запуск мок-сервера
3. Юнит + API тесты
4. Нагрузочное тестирование через JMeter
5. Публикацию отчёта Allure

## 📊 Мониторинг с Grafana
1. JMeter пишет метрики в InfluxDB через Backend Listener
2. Grafana подключается к InfluxDB и показывает данные

## 🧱 Паттерны проектирования
- **Singleton** → `Config`
- **Strategy** → `AuthStrategy`
- **Factory Method** → `RequestFactory`
- **Builder** → `RequestBuilder`
- **Logger** → `logger_util`

## 📎 Зависимости
- Python: `pytest`, `requests`, `allure-pytest`, `flask`
- Jenkins: `allure`, `jmeter`
- JMeter: GUI для генерации `.jmx`
- Grafana + InfluxDB: для визуализации метрик

---

🔥 Полностью масштабируемо, интегрируемо и расширяемо.
