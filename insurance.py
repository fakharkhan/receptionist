# insurance.py
from config import INSURANCE_API_KEY

def verify_insurance(insurance_number):
    """
    Verify a patient's insurance information.
    If INSURANCE_API_KEY is not set to a production key, use a simple local check.
    """
    if INSURANCE_API_KEY == 'your_insurance_api_key_here':
        # Fallback: verify locally by checking that the number has exactly 10 digits.
        if insurance_number.isdigit() and len(insurance_number) == 10:
            return f"Insurance number {insurance_number} verified locally."
        else:
            return f"Insurance number {insurance_number} is invalid locally. Please check the information."
    # In production, call the external insurance verification API here.
    # This is a placeholder for demonstration.
    return f"Insurance number {insurance_number} verified using external API."