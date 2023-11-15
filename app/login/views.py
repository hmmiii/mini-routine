from flask import Blueprint, render_template, Flask, request,make_response,session


login_bp = Blueprint('login', __name__, template_folder='../../templates')


@login_bp.route('/login')
def login():
    context = {
        'title': '미니 루틴 로그인'
    }
    return render_template('login.html', data=context)

@login_bp.route('/join')
def join():
    context = {
        'title': '미니 루틴 로그인'
    }
    return render_template('join.html', data=context)

@login_bp.route('/index')
def index():
    context = {
        'title': '미니 루틴 로그인'
    }
    return render_template('index.html', data=context)

app = Flask(__name__)
app.secret_key = "My_Secret_Key"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == 'POST':
        receive_id = request.form['id']
        session['id'] = receive_id     # 여기
        print(receive_id)
        print(session['id'])

    resp = make_response(render_template('read_cookie.html'))
    resp.set_cookie('id', receive_id)
    return resp


@app.route("/getcookie")
def getcookie():
    user_id = request.cookies.get('id')
    print(id)
    # print(session['user_id'])
    return f'<h1>welcome {id}님</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)











# # sessionStorage를 사용하려면 secret key 값을 주어야 한다.
# MYSECRET = 'this is my key'
# login_bp.secret_key = MYSECRET

# #cookie 조회하기
# login_bp..route('/getcookie/<key>',methods=['POST'])
# def get_cookie(key):
# 	res = request.cookies.get(key)
#     return res


# # make_response를 사용해서 cookie를 set한 페이지를 쉽게 반환해보자
# # make_response(render_template('index.html'))처럼 page를 반환할수 있다.

# @login_bp.route('/setcookie')
# def set_cookie():
# 	key = request.form['key']
#     value = request.form['value']
#     res = make_response('your cookie is create')
#     res.set_cookie(key,value)
#    	# 혹은 간단하게
#     request.cookies.add(key,value)
#     return res

# # cookie 삭제하기
# @login_bp.route('/delete_cookie/<key>')
# def delete_cookie(key):
# 	res = make_response(key+'쿠키가 삭제되었습니다.')
# 	res.delete_cookie(key)
#     #혹은
#     request.cookie.pop(key,None)
#     return res

# # session storage에 저장된 값 조회하기
# @login_bp.route('/getsessiondata/<key>')
# def get_session_data(key):
# 	res = session[key]
#     return res
    
# # session storage에 값 저장하기
# @login_bp.route('/setsessiondata',methods=['POST'])
# def set_session_data():
# 	key = request.form['key']
#     value = request.form['value']
# 	session[key] = value
#     return '저장되었습니다.'

