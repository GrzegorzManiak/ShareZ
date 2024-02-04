from enum import Enum
import datetime


class LogType(Enum):
    INFO = 0
    WARNING = 1
    ERROR = 2

    def __str__(self):
        return self.name


def log(
        log_type: LogType,
        *args,
) -> None:
    """
        Logs a message to the console and to the log file. 
        (TODO: implement log file)

        [TIMESTAMP] [LOG_TYPE]: ARGS...

        Args:
            log_type (LogType): The type of the log
            *args: The message to log

        Returns:
            None
    """

    # -- Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -- Create the log message
    log_message = f"[{timestamp}] [{log_type}]: "
    for arg in args:
        log_message += str(arg) + " "

    # -- Log the message to the console
    print(log_message)
