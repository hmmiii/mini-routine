from flask import Blueprint, render_template, request, redirect, session
from app.models import db, Routine

# 프로젝트 루트 디렉토리 경로
add_bp = Blueprint('add', __name__, template_folder='../../templates')
@add_bp.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':

        # id_receive = request.form.get("id")
        id_receive = session.get('userid', 'Guest')
        content_receive = request.form.get("content")

        routine = Routine(
            id=id_receive,
            check=0,
            content=content_receive
        )

        db.session.add(routine)
        db.session.commit()

        return redirect("../")

    context = {
        'title': '루틴 등록'
    }
    return render_template('add.html', data=context)

