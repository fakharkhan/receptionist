# interaction.py
from tasks import add_task, list_tasks, complete_task
from appointments import schedule_appointment, list_appointments, cancel_appointment
from calls import answer_call, transfer_call, make_real_call
from insurance import verify_insurance
from inquiries import process_inquiry
from logger import log_info, log_error

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
    print("  - 'call real <phone number>' to make a real call via external API")
    print("  - 'verify insurance <insurance number>' to verify insurance information")
    print("  - 'inquire <message>' to process an online inquiry")
    
    while True:
        try:
            user_input = input("Your request (type 'exit' to quit): ").strip()
            log_info(f"Received command: {user_input}")
            lower_input = user_input.lower()
            if lower_input in ['exit', 'quit']:
                print("Thank you for visiting. Have a great day!")
                log_info("Session ended by user.")
                break
            elif lower_input.startswith("add "):
                task_desc = user_input[4:]
                response = add_task(task_desc)
                print(response)
                log_info(f"Added task: {task_desc}")
            elif lower_input == "list tasks":
                response = list_tasks()
                print(response)
                log_info("Listed tasks.")
            elif lower_input.startswith("complete "):
                try:
                    task_number = int(user_input.split()[1])
                    response = complete_task(task_number)
                    print(response)
                    log_info(f"Completed task: {task_number}")
                except (IndexError, ValueError) as e:
                    error_message = "Invalid task number provided for completion."
                    print(error_message)
                    log_error(error_message)
            elif lower_input.startswith("schedule appointment "):
                appointment_detail = user_input[len("schedule appointment "):].strip()
                response = schedule_appointment(appointment_detail)
                print(response)
                log_info(f"Scheduled appointment: {appointment_detail}")
            elif lower_input == "list appointments":
                response = list_appointments()
                print(response)
                log_info("Listed appointments.")
            elif lower_input.startswith("cancel appointment "):
                try:
                    tokens = user_input.split()
                    if len(tokens) < 3:
                        error_message = "No appointment number provided for cancellation."
                        print("Please provide a valid appointment number after 'cancel appointment'.")
                        log_error(error_message)
                        continue
                    appointment_number = int(tokens[2])
                    response = cancel_appointment(appointment_number)
                    print(response)
                    log_info(f"Canceled appointment: {appointment_number}")
                except (IndexError, ValueError):
                    error_message = "Invalid appointment number provided for cancellation."
                    print("Please provide a valid appointment number after 'cancel appointment'.")
                    log_error(error_message)
            elif lower_input == "answer call":
                response = answer_call()
                print(response)
                log_info("Answered call.")
            elif lower_input.startswith("transfer call "):
                department = user_input[len("transfer call "):].strip()
                response = transfer_call(department)
                print(response)
                log_info(f"Transferred call to: {department}")
            elif lower_input.startswith("call real "):
                phone_number = user_input[len("call real "):].strip()
                response = make_real_call(phone_number)
                print(response)
                log_info(f"Made real call to: {phone_number}")
            elif lower_input.startswith("verify insurance "):
                insurance_number = user_input[len("verify insurance "):].strip()
                response = verify_insurance(insurance_number)
                print(response)
                log_info(f"Verified insurance: {insurance_number}")
            elif lower_input.startswith("inquire "):
                inquiry_message = user_input[len("inquire "):].strip()
                response = process_inquiry(inquiry_message)
                print(response)
                log_info(f"Processed inquiry: {inquiry_message}")
            else:
                print("Processing your request... Please hold on.")
                print(f"I've received: '{user_input}'")
                log_info(f"Processed generic request: {user_input}")
        except Exception as e:
            log_error(f"Unhandled exception: {str(e)}")
            print("An error occurred while processing your request. Please try again.")