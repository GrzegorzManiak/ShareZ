"""
    This module is going to be responsible for the editor
    of the application.

    It needs to be able to:
    - Create a window as big to encompass the entire screen (Even if it is a multi-monitor setup)
      so itll overfill outside of the screen (Which is fine)
"""

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)

from logger import log
from server.display_server.main import DisplayServerManager


class EditorWindow(QMainWindow):
    """
        The main window of the editor.
    """

    def __init__(self):
        """
            Creates a new EditorWindow object.
        """

        super().__init__()

        dsm = DisplayServerManager()
        displays = dsm.get_all_displays()
        for display in displays:
            log.info(f"Display: {display}, Size: {display.get_size()}, Position: {display.get_position()}")

        total_size = dsm.calc_total_size()
        log.info(f"Total size: {total_size}")

    # -- Set the window title
        self.setWindowTitle("Screen Capture Editor")

        # -- Create the main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # -- Create the layout
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # -- Create the buttons
        self._capture_button = QPushButton("Capture")
        self._capture_button.clicked.connect(self._capture_button_clicked)
        layout.addWidget(self._capture_button)

        # -- Create the label
        self._label = QLabel("Hello World")
        layout.addWidget(self._label)

    def _capture_button_clicked(self):
        """
            Called when the capture button is clicked.
        """

        self._label.setText("Capture button clicked")