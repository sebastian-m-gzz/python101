from flask import Flask, jsonify, request

app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world'


# http://127.0.0.1:5000/json
@app.route('/json', methods=['GET'])
def json():
    one = {'id': 1, 'name': 'uno'}
    two = {'id': 2, 'name': 'dos'}
    numbers = [one, two]
    return jsonify(numbers)


# http://127.0.0.1:5000/parameters?id=1
@app.route('/parameters', methods=['GET'])
def parameters():
    my_id = request.args.get('id', default=-1, type=int)
    return jsonify(my_id)


app.run(debug=True, host="0.0.0.0")
