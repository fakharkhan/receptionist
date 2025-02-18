# inquiries.py

def process_inquiry(message):
    """
    Process an online inquiry and provide a prompt response.
    For demonstration, this function checks for common keywords and returns a relevant reply.
    """
    lower_message = message.lower()
    if "hours" in lower_message:
        return "Our working hours are from 8 AM to 6 PM, Monday through Friday."
    elif "location" in lower_message:
        return "We are located at 123 Main Street, Anytown, USA."
    elif "insurance" in lower_message:
        return "For insurance-related queries, please provide your insurance number for verification."
    else:
        return "Thank you for your inquiry. We will get back to you shortly."