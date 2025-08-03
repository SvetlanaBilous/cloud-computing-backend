from flask import Flask, request # jsonify
# from keras.models import load_model
# from PIL import Image, ImageOps
# import numpy as np
# import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    print('hello')
    return "<p>Hello World from Svetlana UPDATE 2.8.</p>"

@app.route('/sentiment', methods=['POST'])
def get_sentiment():
    input_data = request.json
    print(input_data)

    return {'input_data': input_data, 'message': 'hello!'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=False)

