from server.display_server.types import DesktopEnvironmentType, DisplayServerType
from logger import log


class BaseDesktop:
    _display_server: DisplayServerType
    _desktop_environment: DesktopEnvironmentType

    def __init__(self,
                 display_server: DisplayServerType,
                 desktop_environment: DesktopEnvironmentType,
                 ):
        """
            Creates a new BaseDesktop object.
        """
        log.info("BaseDesktop.__init__")
        self._display_server = display_server
        self._desktop_environment = desktop_environment

    def get_all_windows(self) -> list:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log.warn("BaseDesktop.get_all_windows is not implemented")
        return []
