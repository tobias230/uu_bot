from bot import Bot

if __name__ == '__main__':
    uu_bot = Bot("https://booking-ra.sshxl.nl/accommodations?returnurl=%2flog-in",
                 "tobias.zenner@gmx.de", "T0b1aS99")

    uu_bot.check_acc_by_url()
