# Sentiment Analysis Application

Это приложение для анализа настроений, написанное на Python с использованием Flask. Оно позволяет пользователям отправлять текст и получать анализ настроения текста в формате JSON.

Используется модель nlptown/bert-base-multilingual-uncased-sentiment
Описание: Эта модель основана на архитектуре BERT (Bidirectional Encoder Representations from Transformers) и обучена для предсказания настроений текстов на различных языках. Она предсказывает оценки настроений в диапазоне от 1 до 5 звезд, где 1 соответствует крайне негативному настроению, а 5 - крайне позитивному.

## Функциональность

- Анализ настроений текста через POST-запрос
- Простая веб-страница для ввода текста и отображения результата анализа настроений

## Установка и запуск

### Установка

1. Склонируйте репозиторий

    ```bash
    git clone https://github.com/milkcookie13/Sentiment-analysis.git
    ```
2. Перейдите в директорию проекта
   
   ```bash
    cd Sentiment-analysis
   ```
    

3. Создайте виртуальное окружение

     - На Windows:
        ```bash
        py -m venv venv
        ```
    - На macOS/Linux:
        ```bash
        python3 -m venv venv
        ```

4. Активируйте виртуальное окружение

    - На Windows:
        ```bash
        venv\Scripts\activate
        ```
    - На macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. Установите зависимости

    ```bash
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

