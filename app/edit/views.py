from flask import Blueprint, render_template, request, redirect
from app.models import db, Routine

# 프로젝트 루트 디렉토리 경로
edit_bp = Blueprint('edit', __name__, template_folder='../../templates')
@edit_bp.route('/edit/<int:rNum>', methods=('GET', 'POST'))
def edit(rNum):
    if request.method == 'POST':
        content_receive = request.form.get("content")

        this_data = Routine.query.filter_by(rNum=rNum).first()
        this_data.content = content_receive

        db.session.add(this_data)
        db.session.commit()

        return redirect("../")
    
    routine_list = Routine.query.all()
    this_routine = Routine.query.filter_by(rNum=rNum).all()
    context = {
        'title': '루틴 수정',
        'routine': this_routine
    }

    # print(this_routine[0].content)
    # print(routine_list[0].content)

    return render_template('edit.html', data=context)

