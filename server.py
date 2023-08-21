from flask import Flask, request, jsonify

app = Flask(__name__)

class Numbers:
    def __init__(self, first, second):
        self.first = first
        self.second = second

class Result:
    def __init__(self, value):
        self.result = value

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    if data and 'first' in data and 'second' in data:
        numbers = Numbers(data['first'], data['second'])
        result = Result(numbers.first + numbers.second)
        return jsonify(result.__dict__)
    else:
        return jsonify(error="Invalid input data"), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    if data and 'first' in data and 'second' in data:
        numbers = Numbers(data['first'], data['second'])
        result = Result(numbers.first - numbers.second)
        return jsonify(result.__dict__)
    else:
        return jsonify(error="Invalid input data"), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
