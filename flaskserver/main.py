from flask import Flask, request, jsonify
#html render
from flask import render_template



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/interaction', methods=['GET'])
def interaction():
    return jsonify({"json":"OK"})

if __name__ == '__main__':
    print("Flask APP is running")
    app.run(debug=True)

