from repositories.task_repository import TaskRepository


class TaskService:
    @staticmethod
    def create_task(title):
        return TaskRepository.create_task(title)

    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_tasks()

    @staticmethod
    def complete_task(task_id):
        return TaskRepository.complete_task(task_id)

    @staticmethod
    def delete_task(task_id):
        return TaskRepository.delete_task(task_id)
