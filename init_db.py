from app import app, db
from models.task_model import Task

with app.app_context():
    db.create_all()
    print("Database initialized.")
