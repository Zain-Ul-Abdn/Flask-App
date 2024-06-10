from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from model import is_unethical

app = Flask("my-app")
CORS(app)

@app.route('/', methods=['OPTIONS', 'POST'])
def index():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers['Access-Control-Allow-Origin'] = 'https://connectifywebapp.azurewebsites.net'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    if request.method == 'POST':
        data = request.get_json()
        input = data.get("data")
        try:
            res = is_unethical(input)
            return jsonify({'response': str(res)})
        except Exception as e:
            return jsonify({'response': "Something went wrong", 'error': e}), 500

if __name__ == '__main__':
    app.run(debug=True)
