import cleaner
import disk_info
import subscription

if subscription.check_subscription():
    print("Действие подписки закончилось, требуется продлить подписку\n")
else:
    before_clean_space = disk_info.get_free_disk_space("D:\\")
    cleaner.clean()
    after_clean_space = disk_info.get_free_disk_space("D:\\")
    disk_info.send_disk_info(before_clean_space, after_clean_space)

input("Нажмите Enter для выхода...")