from flask import Blueprint, render_template, request, session, redirect
from app.models import Routine, db

# 프로젝트 루트 디렉토리 경로
main_bp = Blueprint('main', __name__, template_folder='../../templates')

# 검사할 수 있는 로그인 아이디가 존재하지 않아 우선 루틴만 가지고 옴.
@main_bp.route('/')
def home():
    id = session.get('userid')
    if not id:
        return redirect('/login')
    context = {
        'title': '미니 루틴',
        'routines' : Routine.query.filter_by(id=id).all(),
    }
    return render_template('index.html', data=context)

@main_bp.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    print(data)
    for i in data:
        data = Routine.query.filter_by(rNum=i['rNum']).first()
        data.check = int(i['check'])
        db.session.add(data)
        db.session.commit()
    return 'OK'