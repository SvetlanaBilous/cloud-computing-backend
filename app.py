from flask import Flask, request, jsonify
from textblob import TextBlob
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, origins=["https://cloud-computing-render.onrender.com"])

@app.route("/", methods=["POST"])
def analyze_sentiment():
    input_data = request.json
    text = input_data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        sentiment = 'positive'
    elif polarity < -0.2:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return jsonify({
        'class': sentiment,
        'confidence': round(abs(polarity), 3),
        'input_text': text
    })


@app.route('/status', methods=['GET'])
def status():
    return '''
        <html>
            <head><title>Docker Status</title></head>
            <body style="font-family:sans-serif; text-align:center; padding-top:50px;">
                <h1> Backend is running inside Docker!</h1>
                <p>If you see this page, the Docker container is working as expected.</p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)