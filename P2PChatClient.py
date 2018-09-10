#Import the socket module
import socket
import pickle


from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify

app = Flask(__name__)

#Define port we want to use for connection
port = 5000

#Defind the server we want to connect to
server = '127.0.0.1'

chat = []


@app.route("/", methods=['POST'])
def sendMessage():

    global server
    global chat

    if request.form['message'] != '':
        stringToSend = request.form['message']
        s = socket.socket()
        s.connect((server, port))

        s.send(stringToSend.encode())

        chat = pickle.loads(s.recv(1024))

        s.close()
        return render_template('index.html', chat=chat)

    if request.form['serverWanted'] != '':
        server = request.form['serverWanted']
        s = socket.socket()
        s.connect((server, port))

        s.send(''.encode())

        chat = pickle.loads(s.recv(1024))

        s.close()
        return render_template('index.html', chat=chat)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chat", methods=["GET"])
def getChat():
    response = {'chat': chat, 'length': len(chat)}
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)

