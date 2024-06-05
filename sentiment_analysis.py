from transformers import pipeline
from langdetect import detect

# Загрузка модели и токенизатора
multilingual_sentiment_pipeline = pipeline("sentiment-analysis",
                                           model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text: str) -> dict:
    '''
    :param text:
    :return:
    Возвращает словарь из {Оттенка текста, эмодзи для оттенка, вероятности правильности}
    '''

    result = multilingual_sentiment_pipeline(text)  # Анализ настроения текста с помощью загруженной модели

    label = result[0]['label']  # Получение количества звезд от 1 до 5 для оттенка
    score = result[0]['score']  # вероятность верности ответа
    if label == '1 star':
        sentiment = {'label': 'крайне негативный', 'emoji': '😡', 'score': score}
    elif label == '2 stars':
        sentiment = {'label': 'негативный', 'emoji': '☹️', 'score': score}
    elif label == '3 stars':
        sentiment = {'label': 'нейтральный', 'emoji': '😐', 'score': score}
    elif label == '4 stars':
        sentiment = {'label': 'положительный', 'emoji': '😊', 'score': score}
    elif label == '5 stars':
        sentiment = {'label': 'крайне положительный', 'emoji': '😃', 'score': score}
    else:
        sentiment = {'label': 'UNKNOWN', 'emoji': '❓', 'score': 0.0}

    return sentiment
