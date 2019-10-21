# coding: utf-8
from .. import app, db
from ..models.message import Message
from flask import flash, request, redirect, url_for, make_response
from datetime import datetime


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    sub_form = request.form
    name = sub_form.get("name")
    message = sub_form.get("message")
    in_reg_data = sub_form.get('reg_data')
    # 获取上次提交时间，两次提交间需要间隔30s
    last_time = request.cookies.get('time')
    if last_time is not None:
        last_time = datetime.strptime(last_time, "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_time).seconds < 30:
            flash("留言后，请30s后再来留言！")
            return redirect(url_for('index'))
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
        rsp = make_response(redirect(url_for('index')))
        rsp.set_cookie('time', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return rsp
