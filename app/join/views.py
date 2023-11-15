from flask import render_template, Blueprint, request
import sqlite3
# DB사용하기 위해 import
from app.models import User, db

# 프로젝트 루트 디렉토리 경로
join_bp = Blueprint('join', __name__, template_folder='../../templates')

@join_bp.route('/join', methods=['POST','GET'])
def join() :
    id = ""
    name = ""
    email = ""
    pw = ""
    conpw = ""
    bid = ""

    # input POST 자료 받아옴
    if request.method == 'POST' :
        id = request.form['iid']
        name = request.form['iname']
        email = request.form['iemail']
        pw = request.form['ipw']
        conpw = request.form['iconpw']

        rows = User.query.filter_by(id=id).first()

        if rows is not None :
            # 아이디 중복으로 회원가입 막기
            print(rows)
        else :
            if pw==conpw :
                data = User(id = id, username = name, email = email, pw = pw)
                db.session.add(data)
                db.session.commit()
                return render_template('index.html', data = id)

    context = {"title" : "회원 가입"}
    return render_template('join.html', data = context)
