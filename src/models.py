from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "last_name": self.last_name,
            "age": self.age
        }

    def getAllMembers():
        all_members = Member.query.order_by(Member.age.desc()).all()
        return list(map(lambda x: x.serialize(), all_members))
