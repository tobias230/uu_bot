from bot import Bot

if __name__ == '__main__':
    uu_bot = Bot("https://booking-ra.sshxl.nl/accommodations?returnurl=%2flog-in",
                 "email", "password")

    uu_bot.check_acc_by_url()
