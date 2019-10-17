from .. import app, db
from ..models.message import Message
from flask import render_template, flash, request, redirect, url_for, session
from datetime import datetime


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    sub_form = request.form
    name = sub_form.get("name")
    message = sub_form.get("message")
    in_reg_data = sub_form.get('reg_data')
    reg_data = request.cookies.get('reg_data')
    # 防止爬虫post提交
    if in_reg_data != reg_data or in_reg_data is None or reg_data is None:
        flash("提交状态异常")
        return redirect(url_for('index'))
    # 虽然前端有数据验证，不排除有人用控制台绕过js代码
    # 所以后台也加验证比较好
    if name == '' or message == '':
        flash("姓名或内容不能为空哦")
        return redirect(url_for('index'))
    elif len(message) > 200:
        flash("留言内容过长")
        return redirect(url_for('index'))
    else:
        one_message = Message(name, message, datetime.utcnow())
        db.session.add(one_message)
        db.session.commit()
        flash("你成功地进行了留言^_^~~~")
        return redirect(url_for('index'))
