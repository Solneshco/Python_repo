# Проект тестирования с Allure и PageObject

## Описание проекта
Проект автоматизации тестирования с использованием:
- Page Object Pattern
- Allure для отчетов
- Selenium WebDriver
- Pytest

## Структура проекта
```
lesson_10/
├── pages/          # Page Object классы
├── tests/          # Тесты
├── conftest.py     # Фикстуры pytest
├── pytest.ini      # Конфигурация pytest
└── requirements.txt # Зависимости
```

## Установка и настройка

### 1. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 2. Установите Allure:
#### Для Windows:
```bash
# С помощью Scoop
scoop install allure

# Или скачайте с https://github.com/allure-framework/allure2/releases
```

#### Для MacOS:
```bash
brew install allure
```

#### Для Linux:
```bash
# Ubuntu/Debian
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure

# Или через SDKMAN
sdk install allure
```

## Запуск тестов

### Запуск всех тестов с генерацией Allure отчетов:
```bash
# Создаст директорию allure-results с сырыми данными
pytest

# С указанием конкретной директории
pytest --alluredir=./allure-results
```

### Запуск с определенными тегами:
```bash
# Только критичные тесты
pytest -m "critical"

# По конкретной фиче
pytest -k "login"
```

## Просмотр отчетов

### 1. Генерация HTML отчета:
```bash
# Преобразуем сырые данные в HTML
allure generate ./allure-results -o ./allure-report --clean
```

### 2. Открыть отчет в браузере:
```bash
# Запуск локального сервера
allure serve ./allure-results

# Или откройте сгенерированный отчет
allure open ./allure-report
```

### 3. Просмотр через веб-сервер:
```bash
# Если нужен статический сервер
cd allure-report
python -m http.server 8000
# Открыть http://localhost:8000
```

## Особенности реализации

### 1. Page Object Pattern:
- Каждая страница описана отдельным классом
- Локаторы вынесены в константы
- Методы содержат бизнес-логику

### 2. Allure интеграция:
- Шаги помечены `@allure.step`
- Тесты имеют заголовки `@allure.title`
- Описания `@allure.description`
- Приоритеты `@allure.severity`
- Скриншоты при падениях

### 3. Фикстуры pytest:
- Инициализация WebDriver
- Автоматическое закрытие браузера
- Скриншоты при ошибках

## Генерация разных типов отчетов

### Краткий отчет в консоли:
```bash
pytest -v
```

### HTML отчет pytest:
```bash
pytest --html=report.html --self-contained-html
```

### Allure отчет с историей:
```bash
# Сохранение истории между запусками
allure generate ./allure-results -o ./allure-report --clean
```

## CI/CD интеграция

### Пример для GitHub Actions:
```yaml
name: Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Install Allure
        run: sudo apt-get install allure
      - name: Run tests
        run: pytest --alluredir=./allure-results
      - name: Generate Allure report
        run: allure generate ./allure-results -o ./allure-report --clean
      - name: Upload Allure report
        uses: actions/upload-artifact@v2
        with:
          name: allure-report
          path: ./allure-report
```

## Полезные команды

### Очистка результатов:
```bash
# Очистить результаты перед запуском
rm -rf allure-results allure-report

# Или используйте опцию pytest
pytest --clean-alluredir
```

### Запуск с фильтрацией:
```bash
# По тегам
pytest -m "not slow"

# По имени теста
pytest -k "test_login"

# С определенным уровнем логирования
pytest -v --tb=short
```

## Дополнительная информация

- [Документация Allure](https://docs.qameta.io/allure/)
- [Документация pytest](https://docs.pytest.org/)
- [Документация Selenium](https://www.selenium.dev/documentation/)