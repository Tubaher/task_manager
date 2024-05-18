from flask import Flask
from config import Config
from models import db
from controllers.task_controller import task_bp
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

app.register_blueprint(task_bp, url_prefix="/tasks")


with app.app_context():

    def create_tables():
        db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
