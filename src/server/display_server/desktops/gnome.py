import json

from server.display_server.desktop import BaseDesktop
from server.display_server.types import DesktopEnvironmentType, DisplayServerType
from logger import log
from PySide6.QtDBus import QDBusConnection, QDBusInterface, QDBusMessage, QDBusReply


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

    def close_dbus(self):
        """
            Closes the dbus.
        """
        log.warn("Gnome.close_dbus")

    def get_all_windows(self) -> list:
        """
            Gets all windows.

            Returns:
                list: A list of all windows.
        """
        log.info("Gnome.get_all_windows")

        try:
            reply = self._dbus_interface.call('get_open_windows')
            reply = reply.arguments()[0]

            # -- Parse the reply json
            parsed = []
            for window in reply:
                parsed.append(json.loads(window))
            return parsed

        except Exception as e:
            log.error(f"Error: {e}")
            return []
