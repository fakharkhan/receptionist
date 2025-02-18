# test_receptionist.py
import unittest
from tasks import add_task, list_tasks, complete_task
from appointments import schedule_appointment, list_appointments, cancel_appointment
from insurance import verify_insurance
from inquiries import process_inquiry

# Note: In a real-world scenario, consider using mocks to isolate tests from file I/O.
# For demonstration purposes, this test suite uses the in-memory lists.

class TestTasks(unittest.TestCase):
    def setUp(self):
        # Reset the tasks list (assuming tasks is a global list in tasks.py)
        from tasks import tasks
        tasks.clear()

    def test_add_and_list_tasks(self):
        add_task("Test Task")
        tasks_list = list_tasks()
        self.assertIn("Test Task", tasks_list)

    def test_complete_task(self):
        add_task("Complete this task")
        complete_task(1)
        tasks_list = list_tasks()
        self.assertIn("Done", tasks_list)

class TestAppointments(unittest.TestCase):
    def setUp(self):
        from appointments import appointments
        appointments.clear()

    def test_schedule_and_list_appointments(self):
        schedule_appointment("Meeting with Dr. Smith")
        apps = list_appointments()
        self.assertIn("Meeting with Dr. Smith", apps)

    def test_cancel_appointment(self):
        schedule_appointment("Appointment to cancel")
        cancel_appointment(1)
        apps = list_appointments()
        self.assertNotIn("Appointment to cancel", apps)

class TestInsuranceVerification(unittest.TestCase):
    def test_verify_valid_insurance(self):
        result = verify_insurance("1234567890")
        self.assertIn("verified", result.lower())

    def test_verify_invalid_insurance(self):
        result = verify_insurance("invalid")
        self.assertIn("invalid", result.lower())

class TestInquiryProcessing(unittest.TestCase):
    def test_inquire_hours(self):
        response = process_inquiry("What are your hours?")
        self.assertIn("8 AM to 6 PM", response)

    def test_inquire_generic(self):
        response = process_inquiry("Tell me more about your services")
        self.assertIn("Thank you for your inquiry", response)

if __name__ == '__main__':
    unittest.main()