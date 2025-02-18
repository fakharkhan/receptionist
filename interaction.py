# interaction.py
from tasks import add_task, list_tasks, complete_task
from appointments import schedule_appointment, list_appointments, cancel_appointment
from calls import answer_call, transfer_call
from insurance import verify_insurance
from inquiries import process_inquiry

def run_receptionist():
    print("Welcome! I'm your friendly AI Receptionist.")
    print("I'm here to help. How can I assist you today?")
    print("Available commands:")
    print("  - 'add <task>' to add a task")
    print("  - 'list tasks' to view tasks")
    print("  - 'complete <task number>' to mark a task as done")
    print("  - 'schedule appointment <details>' to schedule an appointment")
    print("  - 'list appointments' to view appointments")
    print("  - 'cancel appointment <appointment number>' to cancel an appointment")
    print("  - 'answer call' to simulate answering an incoming call")
    print("  - 'transfer call <department>' to transfer a call")
    print("  - 'verify insurance <insurance number>' to verify insurance information")
    print("  - 'inquire <message>' to process an online inquiry")
    
    while True:
        user_input = input("Your request (type 'exit' to quit): ").strip()
        lower_input = user_input.lower()
        if lower_input in ['exit', 'quit']:
            print("Thank you for visiting. Have a great day!")
            break
        elif lower_input.startswith("add "):
            task_desc = user_input[4:]
            response = add_task(task_desc)
            print(response)
        elif lower_input == "list tasks":
            response = list_tasks()
            print(response)
        elif lower_input.startswith("complete "):
            try:
                task_number = int(user_input.split()[1])
                response = complete_task(task_number)
                print(response)
            except (IndexError, ValueError):
                print("Please provide a valid task number after 'complete'.")
        elif lower_input.startswith("schedule appointment "):
            appointment_detail = user_input[len("schedule appointment "):].strip()
            response = schedule_appointment(appointment_detail)
            print(response)
        elif lower_input == "list appointments":
            response = list_appointments()
            print(response)
        elif lower_input.startswith("cancel appointment "):
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
        elif lower_input == "answer call":
            response = answer_call()
            print(response)
        elif lower_input.startswith("transfer call "):
            department = user_input[len("transfer call "):].strip()
            response = transfer_call(department)
            print(response)
        elif lower_input.startswith("verify insurance "):
            insurance_number = user_input[len("verify insurance "):].strip()
            response = verify_insurance(insurance_number)
            print(response)
        elif lower_input.startswith("inquire "):
            inquiry_message = user_input[len("inquire "):].strip()
            response = process_inquiry(inquiry_message)
            print(response)
        else:
            # Simulate processing other requests.
            print("Processing your request... Please hold on.")
            print(f"I've received: '{user_input}'")