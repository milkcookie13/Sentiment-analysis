# Sentiment Analysis Application

Это приложение для анализа настроений, написанное на Python с использованием Flask. Оно позволяет пользователям отправлять текст и получать анализ настроения текста в формате JSON.

## Функциональность

- Анализ настроений текста через POST-запрос
- Простая веб-страница для ввода текста и отображения результата анализа настроений

## Установка и запуск

### Установка

1. Склонируйте репозиторий

    ```bash
    git clone https://github.com/ваше-имя-пользователя/ваш-репозиторий.git
    cd ваш-репозиторий
    ```

2. Создайте виртуальное окружение

    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение

    - На Windows:
        ```bash
        venv\Scripts\activate
        ```
    - На macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Установите зависимости

    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

### Запуск приложения

1. Запустите приложение

    ```bash
    python site.py
    ```

2. Откройте браузер и перейдите по адресу

    ```url
    http://127.0.0.1:5000
    ```

## Структура проекта

```bash
.
├── site.py                 # Основной файл приложения Flask
├── sentiment_analysis.py   # Скрипт анализа настроений
├── templates
│   └── index.html          # HTML шаблон для главной страницы
├── requirements.txt        # Файл зависимостей

