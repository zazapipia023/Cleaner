import logging
import os

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

for handler in logging.getLogger().handlers[:]:
    logging.getLogger().removeHandler(handler)

file_handler = logging.FileHandler(os.path.join(log_dir, 'cleaner.log'))
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
