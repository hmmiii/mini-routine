from flask import render_template, Blueprint, request, jsonify, g, session

# DB사용하기 위해 import
from app.models import User, db

# 프로젝트 루트 디렉토리 경로
join_bp = Blueprint('join', __name__, template_folder='../../templates')

@join_bp.route('/checkid', methods=['POST'])
def checkid() :
    id = request.json['id']
    rows = User.query.filter_by(id=id).first()

    if rows is not None :
        return jsonify({"status" : "exist"})
    else :
        return jsonify({"status" : "ok"})


@join_bp.route('/join', methods=['POST','GET'])
def join() :
    joinresult = ""

    # input POST 자료 받아옴
    if request.method == 'POST' :
        id = request.form['iid']
        name = request.form['iname']
        email = request.form['iemail']
        pw = request.form['ipw']
        conpw = request.form['iconpw']

        rows = User.query.filter_by(id=id).first()

        if rows is not None :
            print(rows)
        else :
            if pw==conpw :
                data = User(id = id, username = name, email = email, pw = pw)
                db.session.add(data)
                db.session.commit()
                joinresult = "회원가입 완료! (로그인 후 사용해주세요)"
                # return render_template('index.html')

    context = {"title" : "회원 가입", "joinresult" : joinresult}
    return render_template('join.html', data = context)

    



