"""
    :author: XinJi Zhou
    :last editTime: 2019-10-15
"""
from .. import db
from datetime import datetime


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    content = db.Column(db.String(200))
    submit_time = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    def __init__(self, name, content, time):
        self.name = name
        self.content = content
        self.submit_time = time
