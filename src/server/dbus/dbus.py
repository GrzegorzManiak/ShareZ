from logger import log
from server.dbus.methods import DBusMethods
from server.other import Singleton
from PySide6.QtCore import QFile, QIODevice, QTextStream

from dbus_next.service import ServiceInterface
from dbus_next.aio import MessageBus
from threading import Thread
import asyncio


class ShareZBus(metaclass=Singleton):
    """
        A class that manages the dbus server, it will not
        differ between DEs
    """

    _BUS_NAME = 'dev.grzegorzmaniak.sharez.server'
    _OBJECT_PATH = '/'
    _INTERFACE = 'dev.grzegorzmaniak.sharez.server'
    _IFACE_DIR = './src/iface.xml'

    _dbus: MessageBus
    _interface: ServiceInterface
    _server_thread: Thread

    def __init__(self):
        self._server_thread = Thread(
            target=self._run_server,
            daemon=True
        )

    def _run_server(self):
        """
            You'll have to forgive me for this one, Im not too familiar with
            async code in python (Especially the Async keyword), so I had to
            do this in magical way.
        """
        try:
            async def run():
                # -- Connect to the Session Bus
                self._dbus = await MessageBus().connect()

                # -- Export the interface
                self._interface = DBusMethods(self._INTERFACE)
                self._dbus.export(self._OBJECT_PATH, self._interface)

                # -- Request the bus name
                await self._dbus.request_name(self._BUS_NAME)

                # -- Log and run the event loop
                self.print_dbus_info()
                loop = asyncio.get_event_loop()
                await loop.create_future()

            # -- Start!
            asyncio.run(run())

        except Exception as e:
            log.error(f"DBUS Error: {e}")

    def start(self):
        self._server_thread.start()

    def print_dbus_info(self):
        log.info(f"Bus name: {self._dbus.unique_name}")
        log.info(f"Service Name: {self._interface.introspect().name}")
