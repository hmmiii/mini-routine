from flask import render_template, Blueprint, request
import sqlite3

join_bp = Blueprint('join', __name__, template_folder='../../templates')

# cona = sqlite3.connect('app\database.db')
# cursora = cona.cursor()
# querya = "SELECT * FROM user"
# cursora.execute(querya)
# rowsa = cursora.fetchall()

@join_bp.route('/join', methods=['POST','GET'])
def join() :
    id = ""
    name = ""
    email = ""
    pw = ""
    conpw = ""
    bid = ""

    conn = sqlite3.connect('app\database.db')
    cursor = conn.cursor()

    query = "SELECT id FROM user"
    cursor.execute(query)
    rowa = cursor.fetchall()

    # input POST 자료 받아옴
    if request.method == 'POST' :
        id = request.form['iid']
        name = request.form['iname']
        email = request.form['iemail']
        pw = request.form['ipw']
        conpw = request.form['iconpw']

        select_id = "SELECT * FROM user WHERE id=?"
        cursor.execute(select_id, (id,))
        rows = cursor.fetchall()
        for row in rows :
            if row[0] is not None :
                bid = row[0]
                print(row)
            else :
                if pw==conpw :
                    print(id, name, email, pw, conpw)
                else:
                    print("비밀번호와 비밀번호 확인란이 일치하지 않습니다!")


    
    context = {"rowa" : rowa}

    return render_template('join.html', data = context)
