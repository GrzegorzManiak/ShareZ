from src.server.display_server.desktop import BaseDesktop
from src.server.display_server.types import DesktopEnvironmentType, DisplayServerType
from src.logger import log


# -- Gnome specific imports


class Gnome(BaseDesktop):

    def __init__(self,
                 display_server: DisplayServerType,
                 ):
        """
            Creates a new Gnome object.
        """
        log.info("Gnome.__init__")
        super().__init__(display_server, DesktopEnvironmentType.GNOME)

    def get_all_windows(self) -> list:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log.info("Gnome.get_all_windows")

        return []
