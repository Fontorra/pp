from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
import datetime
import blockChain
import psycopg2
app = Flask(__name__)

conn = psycopg2.connect(database="postgres", user="postgres", host="localhost", password="1234")
cur = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.method )
    try:
        print(id, position)
        return redirect('conspect')
    except:
        print(3)
        if request.method == 'POST':
            login = request.form['login']
            if len(login) < 1:
                return redirect(url_for('index'))
            try:
                password = request.form['password']
            except Exception:
                password = False
            cur.execute('SELECT "Password" FROM public."User" WHERE "Login" = \'%s\'' % login)
            pswd = cur.fetchone()
            print(password, login)
            if pswd == password:
                cur.execute('SELECT position FROM public."User" WHERE "Login" = \'%s\'' % login)
                position = cur.fetchone()
                cur.execute('SELECT id FROM public."User" WHERE "Login" = \'%s\'' % login)
                id = cur.fetchone()
                return render_template('conspect.html', id = id, position = position)
                return redirect('conspect')
        return render_template('index.html')

@app.route('/conspect', methods = ['GET', 'POST'])
def conspect():
    print(1)
    if request.method == 'POST':
        print(2)
        text = request.form['text']
        print(text)
        now = datetime.datetime.now()
        if len(text) < 1:
            return redirect('conspect')
        if position == 1:
            cur.execute('INSERT INTO public."Meta_info" (note_supervisor, id_supervisor, date) VALUES (\'%s\', %s, %s)' % (text, position, now))
        else:
            cur.execute('INSERT INTO public."Meta_info" (note_student_1, student, date) VALUES' (text, position, now))
    return render_template('index.html')
@app.route('/valid', methods = ['GET', 'POST'])
def valid():
    return 1
if __name__ == '__main__':
    app.run(debug=True)
conn.commit()
cur.close()
conn.close()
