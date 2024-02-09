import PySide6.QtCore

from logger import log


class Singleton(type):
    """
        A singleton metaclass I stole from stackoverflow.
        https://stackoverflow.com/a/6798042
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def dir_exists(
        directory: str,
        create: bool = False
) -> bool:
    """
        Checks if a directory exists.
        If create is True, it will create the directory if it does not exist, and if creation
        succeeds, it will return True.

        Args:
            directory (str): The directory to check.
            create (bool): If the directory does not exist, create it.
    """

    # -- Check if the directory exists (Using PySide6.QtCore.QDir)
    if PySide6.QtCore.QDir(directory).exists():
        return True

    # -- If the directory does not exist, and create is True, create the directory
    if create:
        try:
            PySide6.QtCore.QDir().mkpath(directory)
            return PySide6.QtCore.QDir(directory).exists()

        except Exception as e:
            log.error(f"FATAL: Could not create directory: {directory}")
            return False

    return False
