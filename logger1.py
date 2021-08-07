from datetime import datetime


class App_Logger:
    """
        This class shall  be used for logging.

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None

        """
    def __init__(self):
        pass

    def log(self, log_message):
        """
                Method Name: log
                Description: This method logs the message to the logs file
                Output: text message.
                On Failure: None

                Written By: Tejas Jay (TJ)
                Version: 1.0
                Revisions: None

                """
        log_file = open("logs.txt", 'a+')
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        log_file.write(str(self.date) + "\t" + str(self.current_time) + "\t" + log_message +"\n")
        log_file.close()
