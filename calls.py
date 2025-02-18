# calls.py
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER
from twilio.rest import Client

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

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
    Make a real call using Twilio API.
    """
    try:
        call = client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to=to_number,
            from_=TWILIO_PHONE_NUMBER
        )
        return f"Call initiated with SID: {call.sid}"
    except Exception as e:
        return f"Error making call: {str(e)}"