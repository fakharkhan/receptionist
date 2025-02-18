# appointments.py

appointments = []

def schedule_appointment(details):
    """Schedule a new appointment with the provided details."""
    appointments.append({"details": details, "status": "Scheduled"})
    return f"Appointment scheduled: {details}"

def list_appointments():
    """Return a formatted list of scheduled appointments."""
    if not appointments:
        return "No appointments scheduled."
    result = ""
    for idx, app in enumerate(appointments, start=1):
        result += f"{idx}. {app['details']} - {app['status']}\n"
    return result

def cancel_appointment(appointment_number):
    """Cancel a scheduled appointment given its number."""
    if 0 < appointment_number <= len(appointments):
        canceled = appointments.pop(appointment_number - 1)
        return f"Appointment canceled: {canceled['details']}"
    else:
        return "Invalid appointment number."