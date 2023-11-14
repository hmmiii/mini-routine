from flask import render_template, Blueprint, request
import sqlite3

join_bp = Blueprint('join', __name__, template_folder='../../templates')


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
        rows = cursor.fetchone()

        if rows is not None :
            # 아이디 중복으로 회원가입 막기
            print(rows)
        else :
            if pw==conpw :
                insert_data = {(id, name, email, pw)}
                insert_query = "INSERT INTO user (id, username, email, pw) VALUES (?, ?, ?, ?)"
                cursor.executemany(insert_query, insert_data)
                conn.commit()
                conn.close()
                return render_template('index.html', data = id)

    context = {"title" : "회원 가입", "rowa" : rowa}

    return render_template('join.html', data = context)
