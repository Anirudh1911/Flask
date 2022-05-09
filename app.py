from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder='templates')


@app.route('/')
def render():
    return render_template("login.html")


dictionary = {'anirudh': '123', 'admin': 'admin', 'user': 'user'}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    uname = request.form['username']
    pwd = request.form['password']
    if uname not in dictionary:
        return render_template('login.html', info='Invalid User')
    else:
        if dictionary[uname] != pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('redirect.html', name=uname)


if __name__ == '__main__':
    app.run()
