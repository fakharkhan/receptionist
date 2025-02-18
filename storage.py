# storage.py
import json
import os

TASKS_FILE = "tasks.json"
APPOINTMENTS_FILE = "appointments.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def load_appointments():
    if os.path.exists(APPOINTMENTS_FILE):
        with open(APPOINTMENTS_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_appointments(appointments):
    with open(APPOINTMENTS_FILE, "w") as f:
        json.dump(appointments, f)