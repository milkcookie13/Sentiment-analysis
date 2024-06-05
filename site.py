from flask import Flask, render_template, request, jsonify
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

# Маршрут для обработки POST-запроса на анализ настроения
@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    text = request.form['text']  # Получение текста из формы
    sentiment = analyze_sentiment(text)  # Анализ настроения текста
    return jsonify(sentiment) # Возвращение результата в формате JSON

# Маршрут для отображения главной страницы
@app.route('/')
def index():
    return render_template('index.html') # Рендеринг HTML шаблона index.html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Запуск приложения Flask в режиме отладки