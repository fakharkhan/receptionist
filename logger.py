# logger.py
import logging

# Configure logging to output to a file with a specific format
logging.basicConfig(
    filename='receptionist.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)