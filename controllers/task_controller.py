from flask import Blueprint, request, jsonify
from services.task_service import TaskService

task_bp = Blueprint("task_bp", __name__)


@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = TaskService.create_task(data["title"])
    return (
        jsonify(
            {
                "message": "Task created",
                "task": {
                    "id": new_task.id,
                    "title": new_task.title,
                    "completed": new_task.completed,
                },
            }
        ),
        201,
    )


@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = TaskService.get_all_tasks()
    tasks_list = [
        {"id": task.id, "title": task.title, "completed": task.completed}
        for task in tasks
    ]
    return jsonify(tasks_list), 200


@task_bp.route("/<int:id>", methods=["GET"])
def get_task(id):
    task = TaskService.get_task_by_id(id)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    return (
        jsonify(
            {"id": task.id, "title": task.title, "completed": task.completed}
        ),
        200,
    )


@task_bp.route("/<int:id>", methods=["PUT"])
def complete_task(id):
    task = TaskService.complete_task(id)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    return (
        jsonify(
            {
                "message": "Task marked as completed",
                "task": {
                    "id": task.id,
                    "title": task.title,
                    "completed": task.completed,
                },
            }
        ),
        200,
    )


@task_bp.route("/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = TaskService.delete_task(id)
    if not task:
        return jsonify({"message": "Task not found"}), 404
    return jsonify({"message": "Task deleted"}), 200
