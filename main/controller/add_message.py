from .. import app, db
from ..models.message import Message
from flask import render_template

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    one_message = Message('1', 'xinji', '22', '22')
    db.session.add(one_message)
    db.session.commit()
    return render_template('index.html')