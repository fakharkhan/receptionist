# interaction.py
from tasks import add_task, list_tasks, complete_task

def run_receptionist():
    print("Welcome! I'm your friendly AI Receptionist.")
    print("I'm here to help. How can I assist you today?")
    print("You can type commands like 'add <task>', 'list tasks', or 'complete <task number>'.")
    
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
        else:
            # Simulate processing the user's request.
            print("Processing your request... Please hold on.")
            print(f"I've received: '{user_input}'")