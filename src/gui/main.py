
from PySide6.QtWidgets import QComboBox
from PySide6.QtWidgets import (QGridLayout, QLabel, QWidget)
from PySide6.QtCore import Slot

from logger import log
from server.display_server.main import DisplayServerManager
from server.selection.selection import Selection


class SourceSelector(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("SourceSelector.__init__")

        self._source_label = QLabel("Select source to capture:", self)
        self._source_list_view = QComboBox(self)

        self._source_list_view.currentIndexChanged.connect(self._source_selected)

        grid_layout = QGridLayout(self)
        grid_layout.addWidget(self._source_label, 0, 0)
        grid_layout.addWidget(self._source_list_view, 1, 0)

        # -- Onclick of the dropdown update the list of sources:
        self._source_list_view.activated.connect(self._update_source_list)

        dsm = DisplayServerManager()
        windows = dsm.get_all_windows()
        for window in windows:
            self._source_list_view.addItem(window.get_name(), window)

    @Slot()
    def _source_selected(self):
        selected_area = self._source_list_view.currentData()
        if not isinstance(selected_area, Selection): return
        log.info(f"Source selected: {selected_area}, Size: {selected_area.get_size()}, Position: {selected_area.get_position()}")

    @Slot()
    def _update_source_list(self):
        log.info("Updating source list")

        # -- Clear the list
        self._source_list_view.clear()

        # -- Add all windows to the list
        dsm = DisplayServerManager()
        windows = dsm.get_all_windows()
        for window in windows:
            self._source_list_view.addItem(window.get_name(), window)


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("TestWidget.__init__")

        # -- 500x500px window:
        self.resize(500, 500)

        # -- Add a SourceSelector:
        self._source_selector = SourceSelector(self)
