from datetime import datetime


class Logger(object):

    log_file_name = "log/log.txt"
    instance = None

    def __new__(cls):
        if not Logger.instance:
            Logger.instance = object.__new__(cls)
        return Logger.instance

    def inform(self, message):
        f = None
        try:
            f = open(Logger.log_file_name, "a")
            date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M")
            f.write(date_and_time + " >>> " + message + "\n")
        except IOError, e:
            print("info: " + e.args[0])
        finally:
            if f:
                f.close()
        print("info: " + message)
