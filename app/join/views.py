from flask import render_template, Blueprint, request
import sqlite3

join_bp = Blueprint('join', __name__, template_folder='../../templates')

conn = sqlite3.connect('app\database.db')
cursor = conn.cursor()
query = "SELECT * FROM user"
cursor.execute(query)
rows = cursor.fetchall()

@join_bp.route('/join', methods=['POST','GET'])
def join() :
    id = ""
    name = ""
    email = ""
    pw = ""
    conpw = ""

    for row in rows :
        print(row)

    if request.method == 'POST' :
        id = request.form['iid']
        name = request.form['iname']
        email = request.form['iemail']
        pw = request.form['ipw']
        conpw = request.form['iconpw']
        
    if pw==conpw :
        print(id, name, email, pw, conpw)
    


    return render_template('join.html')
