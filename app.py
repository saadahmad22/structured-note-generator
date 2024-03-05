from flask import Flask
from app_resources.views import view


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('./app_resources/config.py', silent=True)

    app.register_blueprint(view)

    return app

app: Flask = create_app()

# serve
if __name__ == '__main__':
    app.run(host=app.config["API_SERVER_HOST"], port=app.config["API_SERVER_PORT"], debug=True)