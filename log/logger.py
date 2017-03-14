from datetime import datetime

LOG_FILE_NAME = "log/log.txt"

__all__ = ["inform"]


def inform(message):
    f = None
    try:
        f = open(LOG_FILE_NAME, "a")
        date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        f.write(date_and_time + " >>> " + message + "\n")
    except IOError as error:
        print("info: " + error.args[0])
    finally:
        if f:
            f.close()
    print("info: " + message)
