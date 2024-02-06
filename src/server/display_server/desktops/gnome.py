from time import sleep

from src.server.display_server.desktop import BaseDesktop
from src.server.display_server.types import DesktopEnvironmentType, DisplayServerType
from src.logger import log
from pydbus import SessionBus


class Gnome(BaseDesktop):
    _BUS_NAME = 'dev.grzegorzmaniak.sharez'
    _OBJECT_PATH = '/dev/grzegorzmaniak/sharez'
    _dbus = SessionBus()

    def __init__(self,
                 display_server: DisplayServerType,
                 ):
        """
            Creates a new Gnome object.
        """
        log.info("Gnome.__init__")
        super().__init__(display_server, DesktopEnvironmentType.GNOME)

        # -- Connect to the dbus:
        log.info(f"Connecting to dbus: {self._BUS_NAME} {self._OBJECT_PATH}")
        try:
            self._dbus = self._dbus.get(
                self._BUS_NAME,
                self._OBJECT_PATH
            )

            log.info(f"Connected to dbus: {self._dbus}")
            log.info(f"Introspect: {self._dbus.Introspect()}")

        except Exception as e:
            log.warn(f"Error connecting to dbus: {e}")


    def get_all_windows(self) -> list:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log.info("Gnome.get_all_windows")

        return []
