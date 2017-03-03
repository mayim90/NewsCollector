from datetime import datetime


class Logger(object):

    def __init__(self, log_file_name):
        self._log_file_name = log_file_name

    def inform(self, message):
        f = None
        try:
            f = open(self._log_file_name, "a")
            date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M")
            f.write(date_and_time + " >>> " + message + "\n")
        except IOError, e:
            print("info: " + e.args[0])
        finally:
            if f:
                f.close()
        print("info: " + message)
