import os
import logging

from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE_NAME)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] - %(lineno)d %(name)s %(levelname)s - %(message)s')

if __name__ == '__main__':
    logging.info("Logger initialized successfully")
