# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')
INSURANCE_API_KEY = os.getenv('INSURANCE_API_KEY')