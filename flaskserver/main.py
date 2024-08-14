from flask import Flask, request, jsonify
#html render
from flask import render_template



app = Flask(__name__)

#decorator function to refuse bot (user agent)
def check_bot(func):
    def wrapper(*args, **kwargs):
        user_agent = request.headers.get('User-Agent')
        if 'bot' in user_agent:
            return jsonify({"success":False, "message":"Bot detected"})
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper




@app.route('/', methods=['GET'])
@check_bot
def home():
    return render_template('index.html')

def openandtraitfile(file):
    f = open(file, 'r')
    data = f.read()
    f.close()
    return data

@app.route('/interaction', methods=['GET'])
@check_bot
def interaction():
    time = openandtraitfile('time.txt')
    temp = openandtraitfile('temp.txt')
    return jsonify({"success":True,"time":time, "temperature":temp})


@app.route('/settemp', methods=['POST','GET'])
@check_bot
def settemp():
    #on recupere le parametre temp (qui est dans le get)
    try:
        temp = request.args.get('temp')
        #verifier si temp est bien un nombre
        try:
            temp = int(temp)
        except:
            return jsonify({"success":False})
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
@check_bot
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


@app.route('/gettemp', methods=['GET'])
@check_bot
def gettemp():
    temp = openandtraitfile('temp.txt')
    return jsonify({"success":True,"temperature":temp})

@app.route('/gettime', methods=['GET'])
@check_bot
def gettime():
    time = openandtraitfile('time.txt')
    return jsonify({"success":True,"time":time})






if __name__ == '__main__':
    print("Flask APP is running")
    app.run(debug=False, host='0.0.0.0', port=5000)


