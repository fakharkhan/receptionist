# tasks.py
from storage import load_tasks, save_tasks

tasks = load_tasks()

def add_task(task_description):
    """Add a new task with a description."""
    tasks.append({"description": task_description, "completed": False})
    save_tasks(tasks)
    return f"Task added: {task_description}"

def list_tasks():
    """Return a formatted list of tasks."""
    if not tasks:
        return "No tasks available."
    task_list = ""
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Pending"
        task_list += f"{idx}. {task['description']} - {status}\n"
    return task_list

def complete_task(task_number):
    """Mark a task as completed based on its number."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        return f"Task {task_number} marked as completed."
    else:
        return "Invalid task number."