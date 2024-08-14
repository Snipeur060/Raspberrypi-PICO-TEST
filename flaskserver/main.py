from flask import Flask, request, jsonify
#html render
from flask import render_template



app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def openandtraitfile(file):
    f = open(file, 'r')
    data = f.read()
    f.close()
    return data

@app.route('/interaction', methods=['GET'])
def interaction():
    time = openandtraitfile('time.txt')
    temp = openandtraitfile('temp.txt')
    return jsonify({"success":True,"time":time, "temperature":temp})


@app.route('/settemp', methods=['POST','GET'])
def settemp():
    #on recupere le parametre temp (qui est dans le get)
    try:
        temp = request.args.get('temp')
        if temp is not None:
            print(temp)
            f = open('temp.txt', 'w')
            f.write(temp)
            f.close()
            return jsonify({"success":True})
        else:
            return jsonify({"success":False})
    except:
        return jsonify({"success":False})


@app.route('/settime', methods=['POST','GET'])
def settime():
    #on recupere le parametre temp (qui est dans le get)
    try:
        temp = request.args.get('time')
        if temp is not None:
            print(temp)
            f = open('time.txt', 'w')
            f.write(temp)
            f.close()
            return jsonify({"success":True})
        else:
            return jsonify({"success":False})
    except:
        return jsonify({"success":False})





if __name__ == '__main__':
    print("Flask APP is running")
    app.run(debug=True)

