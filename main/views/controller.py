"""
    :author: Xinji Zhou
    :last edittime: 2019-10-14
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql.cursors
from main import app
app.secret_key = '123456'
app.debug = True


@app.route('/')
def hello_world():
    if 'user' in session:
        connection2 = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='guestbook',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor2 = connection2.cursor()
        sql2 = "select * from message;"
        cursor2.execute(sql2)
        u = cursor2.fetchall()
        return render_template('index.html', list=u)
    else:
        # return render_template('form.html')
        connection2 = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='guestbook',
                                      charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor2 = connection2.cursor()
        sql2 = "select * from message;"
        cursor2.execute(sql2)
        u = cursor2.fetchall()
        return render_template('index.html', list=u)

"""
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    info = request.form.get("info")
    print(info)
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='guestbook',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    sql = "insert into message values('jiong' ,'%s', '1')" % info
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    flash("你成功地进行了留言^_^~~~")
    return redirect(url_for('hello_world'))
"""

@app.route('/login', methods=['POST', 'GET'])
def login():
    user = request.form.get('tel')
    session['user'] = user
    flash("你成功地进行了留言^_^~~~")
    return redirect(url_for('hello_world'))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('form.html')
