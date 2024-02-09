from PySide6.QtGui import QGuiApplication

from server.display_server.desktops.desktop import BaseDesktop
from server.display_server.types import DesktopEnvironmentType, DisplayServerType
from server.other import Singleton
from logger import log
import os
from server.selection.selection import Selection
from server.selection.type import SourceType


def _get_desktop_environment() -> DesktopEnvironmentType:
    """
        Gets the type of desktop environment.

        Returns:
            DesktopEnvironmentType: The type of desktop environment.
    """

    # -- Get the desktop environment type
    desktop_environment_name = os.environ.get("DESKTOP_SESSION")
    if desktop_environment_name is None:
        desktop_environment_name = os.environ.get("XDG_CURRENT_DESKTOP")

    # -- Ensure that the desktop environment name is not None
    if desktop_environment_name is None:
        log.error("Desktop environment is Unknown")
        return DesktopEnvironmentType.UNKNOWN

    # -- Get the desktop environment type
    log.info(f"Desktop environment: {desktop_environment_name}")
    match desktop_environment_name.lower():
        case 'gnome':
            return DesktopEnvironmentType.GNOME
        case _:
            log.warn("Desktop environment is Unknown")

    # -- Should not happen but just in case
    return DesktopEnvironmentType.UNKNOWN


class DisplayServerManager(metaclass=Singleton):
    """
        A class that manages the display server.
    """

    _display_server_type: DisplayServerType = DisplayServerType.UNKNOWN
    _desktop_environment_type: DesktopEnvironmentType = DesktopEnvironmentType.UNKNOWN
    _desktop: BaseDesktop

    def __init__(self):
        """
            Creates a new DbusManager object.
        """

        log.info("DisplayServerManager.__init__")
        self._display_server_type = self._get_display_server()
        self._desktop_environment_type = _get_desktop_environment()

        # -- Create the desktop object
        match self._desktop_environment_type:
            case DesktopEnvironmentType.GNOME:
                from server.display_server.desktops.gnome import Gnome
                self._desktop = Gnome(self._display_server_type)

            case _:
                self._desktop = BaseDesktop(self._display_server_type, self._desktop_environment_type)

        self._desktop.get_all_windows()

    def _get_display_server(self) -> DisplayServerType:
        """
            Gets the type of display server.

            Returns:
                DisplayServerType: The type of display server.
        """
        # -- If the display server type has already been found
        if self._display_server_type != DisplayServerType.UNKNOWN:
            return self._display_server_type

        # -- Get the display server type
        server_name = QGuiApplication.platformName()
        log.info(f"Display server: {server_name}")
        match server_name.lower():
            case 'xcb':
                return DisplayServerType.X11
            case 'wayland':
                return DisplayServerType.WAYLAND
            case _:
                log.warn("Display server is Unknown")

        # -- Should not happen but just in case
        return DisplayServerType.UNKNOWN

    def get_all_windows(self) -> list[Selection]:
        """
            Gets all windows that are open on the computer.

            Returns:
                List[QWindow]: A list of all windows that are open on the computer.
        """

        log.info("DisplayServerManager.get_all_windows")
        return self._desktop.get_all_windows()

    def get_all_displays(self) -> list[Selection]:
        """
            Gets all displays that are connected to the computer.

            Returns:
                List[QScreen]: A list of all displays that are connected to the computer.
        """

        log.info("DisplayServerManager.get_all_displays")
        return self._desktop.get_all_displays()

    def calc_total_size(self) -> tuple[tuple[int, int], tuple[int, int]]:
        """
            Calculates the total size of all the displays.

            Returns:
                tuple[tuple[int, int], tuple[int, int]]: The total size of all the displays.
        """

        log.info("DisplayServerManager.calc_total_size")
        displays = self.get_all_displays()

        # -- Top left corner
        max_x = 0
        max_y = 0

        # -- Bottom right corner
        min_x = 0
        min_y = 0

        for display in displays:
            max_x = max(max_x, display.x())
            max_y = max(max_y, display.y())

            min_x = min(min_x, display.x() + display.width())
            min_y = min(min_y, display.y() + display.height())

        return (max_x, max_y), (min_x, min_y)
