from flask import Flask, request, jsonify
app = Flask("my-app")

@app.route('/', methods = ['POST']) 
def index(): 
    data = request.get_json()
    val = data.get("data")
    return val,200

if __name__ == '__main__':
    app.run(debug=True)