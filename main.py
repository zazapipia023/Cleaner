import cleaner
import disk_info
import subscription
from logging_config import logger

print("Производится очистка компьютера, дождитесь окончания очистки")
logger.info("Cleaning has started")
cleaner.clean()
logger.info("Cleaning is complete")

input("Нажмите Enter для выхода")
