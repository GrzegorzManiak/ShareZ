from server.display_server.types import DesktopEnvironmentType, DisplayServerType
from logger import log
from server.selection.selection import Selection


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

    def get_all_windows(self) -> list[Selection]:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log.warn("BaseDesktop.get_all_windows is not implemented")
        return []

    def get_all_displays(self) -> list[Selection]:
        """
            Gets all displays.

            Returns:
                list: A list of all displays.
        """
        log.warn("BaseDesktop.get_all_displays is not implemented")
        return []

    def get_active_display(self) -> None or Selection:
        """
            Gets the active display.

            Returns:
                Selection: The active display.
        """
        log.warn("BaseDesktop.get_active_display is not implemented")
        return None

    def take_screenshot(self) -> str:
        """
            Each DE has its own way of taking a screenshot, most
            can do it trough dbus org.freedesktop.ScreenCast/Screenshot
            but, each DE might have some quirks, therefore this
            function is left to be implemented by the DE specific class.

            Returns:
                str: The path to the screenshot.
        """

        log.warn("BaseDesktop.take_screenshot is not implemented")
        return ''
