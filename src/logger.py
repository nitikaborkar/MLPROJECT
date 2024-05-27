import os
import logging
from datetime import datetime

# Generate the log filename with timestamp
LOG_FILE = f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.log'

# Create the logs directory path
logs_dir = os.path.join(os.getcwd(), 'logs')

# Ensure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s:%(lineno)d] %(message)s',
)


