# interaction.py
from tasks import add_task, list_tasks, complete_task
from appointments import schedule_appointment, list_appointments, cancel_appointment

def run_receptionist():
    print("Welcome! I'm your friendly AI Receptionist.")
    print("I'm here to help. How can I assist you today?")
    print("You can type commands like 'add <task>', 'list tasks', 'complete <task number>',")
    print("'schedule appointment <details>', 'list appointments', or 'cancel appointment <appointment number>'.")
    
    while True:
        user_input = input("Your request (type 'exit' to quit): ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Thank you for visiting. Have a great day!")
            break
        elif user_input.lower().startswith("add "):
            task_desc = user_input[4:]
            response = add_task(task_desc)
            print(response)
        elif user_input.lower() == "list tasks":
            response = list_tasks()
            print(response)
        elif user_input.lower().startswith("complete "):
            try:
                task_number = int(user_input.split()[1])
                response = complete_task(task_number)
                print(response)
            except (IndexError, ValueError):
                print("Please provide a valid task number after 'complete'.")
        elif user_input.lower().startswith("schedule appointment "):
            appointment_detail = user_input[len("schedule appointment "):].strip()
            response = schedule_appointment(appointment_detail)
            print(response)
        elif user_input.lower() == "list appointments":
            response = list_appointments()
            print(response)
        elif user_input.lower().startswith("cancel appointment "):
            try:
                tokens = user_input.split()
                if len(tokens) < 3:
                    print("Please provide a valid appointment number after 'cancel appointment'.")
                    continue
                appointment_number = int(tokens[2])
                response = cancel_appointment(appointment_number)
                print(response)
            except (IndexError, ValueError):
                print("Please provide a valid appointment number after 'cancel appointment'.")
        else:
            # Simulate processing the user's request.
            print("Processing your request... Please hold on.")
            print(f"I've received: '{user_input}'")