from flask import Flask, request, jsonify
app = Flask("my-app")

from model import is_unethical

@app.route('/', methods = ['POST']) 
def index(): 
   data = request.get_json()
   input = data.get("data")
   try:
       res = is_unethical(input)
       return jsonify({'response': str(res)})
   except:
        return jsonify({'response': "Something went wrong"})

if __name__ == '__main__':
    app.run(debug=True)