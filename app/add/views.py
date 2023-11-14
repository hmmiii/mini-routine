from flask import Blueprint, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 직접 속성을 설정
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')
db_uri = f'sqlite:///{db_path}'

class Routine(db.Model):
    rNum = db.Column(db.Integer, primary_key=True, index=True)
    id = db.Column(db.ForeignKey('user.id'), nullable=False)
    check = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)

# 프로젝트 루트 디렉토리 경로
add_bp = Blueprint('add', __name__, template_folder='../../templates')
@add_bp.route('/add', methods=('GET', 'POST'))
def add():

    if request.method == 'POST':
        id_receive = request.args.get("id")
        content_receive = request.args.get("content")

        routine = Routine(
            id=id_receive,
            check=0,
            content=content_receive
        )

        db.session.add(routine)
        db.session.commit()

        return redirect("../")
    

    print("dd")
    context = {
        'title': '미니 루틴 등록'
    }
    return render_template('add.html', data=context)

