from flask import Flask
from sqlalchemy import text
from app.utils.db_initializer import db, ma

app = Flask(__name__, static_folder='public')


class Tokens(db.Model):
    __table_name__ = 'tokens'
    id = db.Column(db.Integer, primary_key=True)
    token_name = db.Column(db.String(255), unique=True)
    used_count = db.Column(db.BIGINT, default=0)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def custom_query(self, query):
        sql = text(query)
        result = db.engine.execute(sql)
        return result

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TokenListSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("token_name", "used_count")
