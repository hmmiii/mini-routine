from flask import render_template, Blueprint

join_bp = Blueprint('join', __name__, template_folder='../../templates')

@join_bp.route('/join')
def join() :
    return render_template('join.html')

