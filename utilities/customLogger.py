import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",  # Specify the log file path
                            format='%(asctime)s: %(levelname)s: %(message)s',  # Log format
                            datefmt='%m/%d/%Y %I:%M:%S %p',  # Date format
                            level=logging.INFO)  # Set the logging level to INFO
        logger = logging.getLogger()
        return logger
