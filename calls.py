# calls.py
from config import TWILIO_API_KEY

def answer_call():
    """
    Simulate answering an incoming call with a polite greeting.
    """
    return "Answering the call... Hello, thank you for calling. How may I assist you today?"

def transfer_call(department="general"):
    """
    Simulate transferring the call to a specified department.
    """
    return f"Transferring your call to the {department} department. Please hold on."

def make_real_call(to_number):
    """
    Simulate making a real call using an external API (e.g., Twilio).
    For production, ensure your TWILIO_API_KEY is set correctly.
    """
    if TWILIO_API_KEY == 'your_twilio_api_key_here':
        return "Twilio API key not set. Please configure your TWILIO_API_KEY for production."
    # In production, call the external API here.
    # This is a placeholder for demonstration.
    return f"Calling {to_number} using Twilio API."