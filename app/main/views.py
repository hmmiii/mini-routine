from flask import Blueprint, render_template
import os

# 프로젝트 루트 디렉토리 경로
main_bp = Blueprint('main', __name__, template_folder='../../templates')

@main_bp.route('/')
def home():
    context = {
        'title': '미니 루틴'
    }
    return render_template('index.html', data=context)
