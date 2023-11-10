from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()

# 직접 속성을 설정
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
db_uri = f'sqlite:///{db_path}'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pw = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

