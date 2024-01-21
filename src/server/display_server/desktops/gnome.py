from server.display_server.desktop import BaseDesktop
from server.display_server.types import DesktopEnvironmentType, DisplayServerType
from log import log, LogType

# -- Gnome specific imports

 

class Gnome(BaseDesktop):

    def __init__(self, 
        display_server: DisplayServerType,
    ):
        """
            Creates a new Gnome object.
        """
        log(LogType.INFO, "Gnome.__init__")
        super().__init__(display_server, DesktopEnvironmentType.GNOME)


        

    def get_all_windows(self) -> list:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log(LogType.INFO, "Gnome.get_all_windows")

 
        return []