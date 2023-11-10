from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'title': '미니루틴'
    }
    return render_template('index.html', data=context)


if __name__ == '__main__':
    app.run(debug=True)
