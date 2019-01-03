from flask import Flask, render_template, redirect, request, url_for , g , session
from model import User
import sqlite3

app = Flask(__name__)

'''sqlite3 数据库'''
app.config["DATABASE"] = 'database.db'
app.config["SECRET_KEY"] = 'fanmaowei'

def connect_db():
    db = sqlite3.connect(app.config['DATABASE'])
    return db

def init_db():
    with app.app_context():
        db = connect_db()
        with app.open_resource('schema.sql',mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # if request.form.to_dict().get('login') != None:
        useremail = request.form["user_email"]
        userpwd = request.form["user_pwd"]
        if useremail == 'fmw19990718@qq.com' and userpwd == '19990718':
            session["user_email"] = useremail
            return redirect('/')
    return render_template('login.html')

def insert_user_to_db(user):
    sql_insert = "insert into users (email, pwd) values (?, ?)"
    args = [user.email, user.pwd]
    g.db.execute(sql_insert, args)
    g.db.commit()

@app.route('/regist', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        user = User()
        user.email = request.form["user_email"]
        user.pwd = request.form["user_pwd"]
        # insert_user_to_db(user)
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
