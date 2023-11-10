from flask import Flask
from app.models import db, db_uri
from app.login.views import login_bp
from app.main.views import main_bp


def create_app():
    app = Flask(__name__)

    # 데이터베이스 URI 설정
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    # 데이터베이스 초기화
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(login_bp)
    app.register_blueprint(main_bp)

    return app

