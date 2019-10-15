from .. import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    content = db.Column(db.String(200))
    submit_time = db.Column(db.DateTime)

    def __init__(self, id, name, content, time):
        self.id = id
        self.name = name
        self.content = content
        self.time = time
