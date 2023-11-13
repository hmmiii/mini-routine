from flask import Flask, render_template, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
import os


# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'database.db')
# db = SQLAlchemy(app)
# from app import db, user

join_bp = Blueprint('join', __name__, template_folder='../../templates')

@join_bp.route('/join', methods=['POST','GET'])
def join() :
    id = ""
    name = ""
    email = ""
    pw = ""
    conpw = ""
    
    if request.method == 'POST' :
        id = request.form['iid']
        name = request.form['iname']
        email = request.form['iemail']
        pw = request.form['ipw']
        conpw = request.form['iconpw']
        
    if pw==conpw :
        print(id, name, email, pw, conpw)
    
    # userinfo = user(id=id, username=name, email=email, pw=pw)
    # db.session.add(userinfo)

    return render_template('join.html')
