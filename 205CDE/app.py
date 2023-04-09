#!/home/alive/205CDE/bin/python
from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)

import pymysql



mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="135135hk",
  database="hw"
)



@app.route('/')
def index():
    return render_template('index(v3).html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/design')
def design():
    return render_template('design.html')
@app.route('/help')
def help():
    return render_template('help.html')
@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')
@app.route('/logged')
def logged():
    return render_template('logged.html')


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        
        name = request.form['login_name']
        password = request.form['password']

        #search through database
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM login WHERE login_name = %s AND password = %s", (name, password))
        result = mycursor.fetchone()

        if result:
            # have hhis account, then lead to the page
            return redirect('/logged')
        else:
            #cannot find,show
            return render_template('logged.html', message='account not found！')
    else:
        # first time login
        return render_template('login1.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
    


