from .. import app, db
from ..models.message import Message
from flask import render_template, flash, request, redirect, url_for
from datetime import datetime


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    sub_form = request.form
    one_message = Message(sub_form.get("name"), sub_form.get("message"), datetime.now())
    db.session.add(one_message)
    db.session.commit()
    flash("你成功地进行了留言^_^~~~")
    return redirect(url_for('index'))
