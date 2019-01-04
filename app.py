from flask import Flask, render_template, redirect, request, url_for , g , session
from model import User
import sqlite3

app = Flask(__name__)

app.config["SECRET_KEY"] = 'fanmaowei'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # if request.form.to_dict().get('login') != None:
        useremail = request.form["user_email"]
        userpwd = request.form["user_pwd"]
        ''' 文件匹配账户信息 '''
        f = open('users_info.text', 'r')
        lines = f.readlines()
        email_info = []
        pwd_info = []
        for i in range(0, len(lines)):
            info = lines[i].split()
            email_info.append(info[0])
            pwd_info.append(info[1])
        f.close()
        ''' 文件匹配账户信息 '''
        for i in range(0, len(lines)):
            if useremail == email_info[i] and userpwd == pwd_info[i]:
                session["user_email"] = useremail
                return redirect('/')
    return render_template('login.html')

@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        user = User()
        user.email = request.form["user_email"]
        user.pwd = request.form["user_pwd"]
        with open('users_info.text', 'a', encoding='utf-8') as fp:
            fp.write(user.email + ' ' + user.pwd + '\n')
        return redirect(url_for("login",useremail=user.email))
    return render_template('regist.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_email', None)
    return redirect('/')

@app.route('/center', methods=['GET', 'POST'])
def center():
    return render_template('center.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
