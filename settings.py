import os
from datetime import datetime
from dotenv import load_dotenv
import logging

load_dotenv()

log_path = os.getenv('log_path')
log_path = datetime.now().strftime(log_path)

logging.basicConfig(filename=log_path, filemode='a',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
