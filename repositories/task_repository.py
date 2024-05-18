from models.task_model import Task
from models import db


class TaskRepository:
    @staticmethod
    def create_task(title):
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    @staticmethod
    def get_all_tasks():
        return Task.query.all()

    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)

    @staticmethod
    def complete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            task.completed = True
            db.session.commit()
        return task

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return task
