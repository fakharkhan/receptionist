# insurance.py

def verify_insurance(insurance_number):
    """
    Simulate verifying a patient's insurance information.
    For demonstration, an insurance number is considered valid if it's exactly 10 digits.
    """
    if insurance_number.isdigit() and len(insurance_number) == 10:
        return f"Insurance number {insurance_number} verified."
    else:
        return f"Insurance number {insurance_number} is invalid. Please check the information and try again."