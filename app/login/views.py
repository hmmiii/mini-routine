from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__, template_folder='../../templates')


@login_bp.route('/login')
def login():
    context = {
        'title': '미니 루틴 로그인'
    }
    return render_template('index.html', data=context)
