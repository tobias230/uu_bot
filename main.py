from bot import Bot

if __name__ == '__main__':
    uu_bot = Bot("https://booking-ra.sshxl.nl/accommodations",
                 "tobias.zenner@gmx.de")

    uu_bot.check_acc_by_url()

    print("test")
    print("moer test")
