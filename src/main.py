from enum import Enum
import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QWidget, QComboBox, QListView,
                               QLabel, QGridLayout, QPushButton, QListView)

from PySide6.QtWidgets import (QGridLayout, QLabel, QListView,
                               QMessageBox, QPushButton, QWidget)
from PySide6.QtGui import QAction, QGuiApplication
from PySide6.QtCore import QItemSelection, Qt, Slot

from logger import log
from server.display_server.main import DisplayServerManager


class SourceSelector(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("SourceSelector.__init__")

        self._source_label = QLabel("Select source to capture:", self)
        self._source_list_view = QComboBox(self)
        self._source_list_view.addItem("Select source to capture:")
        self._source_list_view.addItem("Screen")
        self._source_list_view.addItem("Window")
        self._source_list_view.addItem("Area")

        self._source_list_view.currentIndexChanged.connect(self._source_selected)

        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self._source_label, 0, 0)
        grid_layout.addWidget(self._source_list_view, 1, 0)

        # -- Onclick of the dropdown update the list of sources:
        self._source_list_view.activated.connect(self._update_source_list)

        dsm = DisplayServerManager()
        windows = dsm.get_all_windows()
        log.info(f"Windows: {windows}")
        for window in windows:
            log.info(f"Window: {window}")

    @Slot()
    def _source_selected(self):
        log.info(f"Source selected: {self._source_list_view.currentText()}")

    @Slot()
    def _update_source_list(self):
        log.info("Updating source list")
        dsm = DisplayServerManager()
        windows = dsm.get_all_windows()
        log.info(f"Windows: {windows}")
        for window in windows:
            log.info(f"Window: {window}")


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("TestWidget.__init__")

        # -- 500x500px window:
        self.resize(500, 500)

        # -- Add a SourceSelector:
        self._source_selector = SourceSelector(self)


def main() -> None:
    log.info("Application started")
    app = QApplication(sys.argv)
    QCoreApplication.setApplicationName("ShareZ")
    QCoreApplication.setOrganizationName("Grzegorz.ie")
    QCoreApplication.setApplicationVersion("0.1")

    # -- Create main window:
    main_window = MainWindow()
    main_window.show()

    # -- Execute application:
    app.exec()
    sys.exit(log.info("Application exited"))


if __name__ == "__main__":
    main()
