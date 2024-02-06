import json

from server.display_server.desktops.desktop import BaseDesktop
from server.display_server.types import DesktopEnvironmentType, DisplayServerType
from logger import log
from PySide6.QtDBus import QDBusConnection, QDBusInterface

from server.selection.selection import Selection
from server.selection.type import SourceType


class Gnome(BaseDesktop):
    _BUS_NAME = 'dev.grzegorzmaniak.sharez'
    _OBJECT_PATH = '/dev/grzegorzmaniak/sharez'
    _INTERFACE = 'dev.grzegorzmaniak.sharez'

    _dbus_interface: QDBusInterface
    _dbus_connection: QDBusConnection

    def __init__(self, display_server: DisplayServerType):
        """
            Creates a new Gnome object.
        """
        log.info("Gnome.__init__")
        super().__init__(display_server, DesktopEnvironmentType.GNOME)
        self.connect_to_dbus()

    def connect_to_dbus(self):
        """
            Connects to the dbus.
        """
        log.info("Gnome.connect_to_dbus")
        self._dbus_connection = QDBusConnection.sessionBus()
        self._dbus_interface = QDBusInterface(
            self._BUS_NAME,
            self._OBJECT_PATH,
            self._INTERFACE,
            self._dbus_connection
        )

        self.print_dbus_info()

    def print_dbus_info(self):
        log.info("------------------- Gnome.print_dbus_info -------------------")

        log.info(f"Services")
        services = self._dbus_connection.interface().registeredServiceNames()
        for service in services.value():
            log.info(f"- Service: {service}")

        log.info(f"Bus name: {self._dbus_interface.service()}")
        log.info(f"Object path: {self._dbus_interface.path()}")
        log.info(f"Interface: {self._dbus_interface.interface()}")

        log.info(f"Connection: {self._dbus_connection.isConnected()}")
        log.info(f"Is valid: {self._dbus_interface.isValid()}")

        log.info("------------------- Gnome.print_dbus_info -------------------")

    def get_all_windows(self) -> list[Selection]:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log.info("Gnome.get_all_windows")

        try:
            # -- Call the dbus method
            reply = self._dbus_interface.call('get_open_windows')
            reply = reply.arguments()[0]

            # -- Parse the reply json
            parsed: list[Selection] = []
            for window in reply:
                parsed_window = json.loads(window)
                parsed.append(Selection(
                    SourceType.AREA,
                    x=parsed_window['_x'],
                    y=parsed_window['_y'],
                    width=parsed_window['_width'],
                    height=parsed_window['_height'],
                    friendly_name=parsed_window['_title'],
                    z=parsed_window['_z_index']
                ))

            # -- Return the parsed windows
            return parsed

        except Exception as e:
            log.error(f"Error: {e}")
            return []

    def get_all_displays(self) -> list[Selection]:
        """
            Gets all displays.

            Returns:
                list: A list of all displays.
        """
        log.info("Gnome.get_all_displays")

        try:
            # -- Call the dbus method
            reply = self._dbus_interface.call('get_all_displays')
            reply = reply.arguments()[0]

            # -- Parse the reply json
            parsed: list[Selection] = []
            count = 0
            for display in reply:
                parsed_display = json.loads(display)
                parsed.append(Selection(
                    SourceType.SCREEN,
                    x=parsed_display['_x'],
                    y=parsed_display['_y'],
                    width=parsed_display['_width'],
                    height=parsed_display['_height'],
                    friendly_name=f"Display {count}",
                ))

            # -- Return the parsed displays
            return parsed

        except Exception as e:
            log.error(f"Error: {e}")
            return []