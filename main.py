import cleaner
import disk_info
import subscription
from logging_config import logger

if subscription.check_subscription() == "True":
    print("Действие подписки закончилось, требуется продлить подписку\n")
    logger.info("Cleaning has not started, subscription expired")
else:
    print("Производится очистка компьютера, дождитесь окончания очистки")
    logger.info("Cleaning has started")
    before_clean_space = disk_info.get_free_disk_space("D:\\")
    cleaner.clean()
    after_clean_space = disk_info.get_free_disk_space("D:\\")
    disk_info.send_disk_info(before_clean_space, after_clean_space)
    logger.info("Cleaning is complete")

input("Очистка завершена, нажмите Enter для выхода")
