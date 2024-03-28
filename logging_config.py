import logging
import os

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

if not any(isinstance(handler, logging.FileHandler) for handler in logging.getLogger().handlers):
    logging.basicConfig(
        filename=os.path.join(log_dir, 'cleaner.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    file_handler = logging.FileHandler(os.path.join(log_dir, 'cleaner.log'))
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(file_handler)
