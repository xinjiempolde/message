# coding: utf-8
"""
    :author: Xinji Zhou
    :last edittime: 2019-10-14
"""
from flask import render_template, make_response, request
from main import app
from ..models.message import Message
from datetime import datetime
import random
import string


@app.route('/')
def index():
    if request.user_agent.browser != 'chrome' or request.user_agent.browser != 'firefox':
        return render_template('erros/browser.html')
    # 时间最新的在前面
    messages = Message.query.order_by(Message.submit_time.desc()).all()
    reg_data = ''.join(random.sample(string.ascii_letters + string.digits, 60))
    resp = make_response(render_template('index.html', messages=messages, current_time=datetime.utcnow(), reg_data=reg_data))
    resp.set_cookie('reg_data', reg_data)
    return resp
