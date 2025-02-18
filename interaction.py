# interaction.py

def run_receptionist():
    print("Welcome! I'm your friendly AI Receptionist.")
    print("I'm here to help. How can I assist you today?")
    
    while True:
        user_input = input("Your request (type 'exit' to quit): ")
        if user_input.lower() in ['exit', 'quit']:
            print("Thank you for visiting. Have a great day!")
            break
        else:
            # Simulate processing the user's request.
            print("Processing your request... Please hold on.")
            # For now, we'll just echo the user's message.
            print(f"I've received: '{user_input}'")