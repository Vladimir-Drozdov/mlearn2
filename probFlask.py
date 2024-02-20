from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
"""CORS.cross_origin(
origins = '*',
methods = ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT'],
headers = None,
supports_credentials = False,
max_age = None,
send_wildcard = True,
always_send = True,
automatic_options = False
)"""
@app.route('/probFlask.py', methods=['POST'])
#@cross_origin()
def python_script():
    data = request.get_json()
    variable = data.get('variable')

    # Обработка переменной variable

    # Возвращение ответа
    response = {'result': 'Ответ от Python'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3000)