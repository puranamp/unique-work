from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Routine(db.Model):
    __tablename__ = 'routines'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    content = db.Column(db.String(1028))
    created_at = db.Column(db.DateTime)

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Routine: {}, Username: {}, Time Created: {}>".format(self.content, self.name, self.created_at)
