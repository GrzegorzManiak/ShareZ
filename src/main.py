import sys
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication
from gui.editor.main import EditorWindow
from gui.main import MainWindow
from logger import log
from server.dbus.dbus import ShareZBus


def main() -> None:
    log.info("Application started")
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("ShareZ")
    QCoreApplication.setOrganizationName("Grzegorz.ie")
    QCoreApplication.setApplicationVersion("0.1")

    # -- Create the DBUS server:
    dbus_server = ShareZBus()
    dbus_server.start()

    # -- Create main window:
    main_window = MainWindow()
    main_window.show()

    # editor_window = EditorWindow()
    # editor_window.show()

    # -- Execute application:
    app.exec()
    sys.exit(log.info("Application exited"))


if __name__ == "__main__":
    main()
