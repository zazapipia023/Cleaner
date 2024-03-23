import cleaner
import disk_info
import subscription
import logging.config

if subscription.check_subscription():
    print("Действие подписки закончилось, требуется продлить подписку\n")
    logging.info("Cleaning has not started, subscription expired")
else:
    print("Производится очистка компьютера, дождитесь окончания очистки")
    logging.info("Cleaning has started")
    before_clean_space = disk_info.get_free_disk_space("D:\\")
    cleaner.clean()
    after_clean_space = disk_info.get_free_disk_space("D:\\")
    disk_info.send_disk_info(before_clean_space, after_clean_space)
    logging.info("Cleaning is complete")

input("Очистка завершена, нажмите Enter для выхода")
