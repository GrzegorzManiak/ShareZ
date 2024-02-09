from typing import Tuple
from logger import log
import os
from server.other import dir_exists
from dbus_next.service import ServiceInterface, method


class DBusMethods(ServiceInterface):
    """
        A class that contains methods that are used by the DBus server.
    """

    def __init__(self, name: str):
        """
            Creates a new DBusMethods object.
        """
        super().__init__(name)
        log.info("DBusMethods.__init__")

    @method()
    def get_directories(self) -> 'sss':
        """
            Gets a list of directories where screenshots and recordings
            should be stored.

            Returns:
                Tuple[str, str, str]: A tuple of directories.
                screenshots: The directory where screenshots should be stored.
                recordings: The directory where recordings should be stored.
                temp: The directory where temporary files should be stored.
        """

        log.info("get_directories")
        home_dir = os.path.expanduser("~")

        # TODO: Change this over to load from a config file, for now
        #       we will just use the default directories.
        screenshots = os.path.join(home_dir, "Pictures", "ShareZ")
        recordings = os.path.join(home_dir, "Videos", "ShareZ")
        temp = os.path.join(home_dir, "sharez_tmp")

        # -- Ensure the directories exist
        dir_exists(screenshots, True)
        dir_exists(recordings, True)
        dir_exists(temp, True)

        # -- Return the directories
        return [
            screenshots,
            recordings,
            temp
        ]

    # TODO: get_config, set_config functions
