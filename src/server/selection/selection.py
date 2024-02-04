from src.logger import log
from PySide6.QtGui import QScreen, QWindow
from src.server.selection.type import SourceType, CaptureType


class Selection:
    _source: SourceType
    _screen: QScreen
    _window: QWindow | None
    _friendly_name: str | None = None

    _x: int = 0
    _y: int = 0

    _width: int = 0
    _height: int = 0

    def __init__(self,
                 source: SourceType,
                 capture: CaptureType,
                 screen: QScreen,
                 window: QWindow | None = None,
                 x: int | None = None,
                 y: int | None = None,
                 width: int | None = None,
                 height: int | None = None
                 ):
        """
            Creates a new Area object.

            Args:
                source (SourceType): The type of source that is or has been selected.
                capture (CaptureType): The type of capture that is about to occure.
                screen (QScreen): The screen that is or has been selected.
                window (QWindow): The window that is or has been selected.
                x (int): The x position of the area.
                y (int): The y position of the area.
                width (int): The width of the area.
                height (int): The height of the area.
        """

        self._type = source
        self._capture = capture
        self._screen = screen
        self._window = window

        # -- Auto assign the x, y, width and height if
        #    they are not provided depending on the
        #    source type
        match source:

            case SourceType.SCREEN:

                # -- Screen is simple enough
                self._x = 0
                self._y = 0
                self._width = screen.size().width()
                self._height = screen.size().height()
                self._friendly_name = screen.name()

            case SourceType.WINDOW:

                # -- Ensure that the window is not None
                if window is None:
                    log.error("Window is None")
                    pass

                position = window.position()
                size = window.size()

                self._x = position.x()
                self._y = position.y()
                self._width = size.width()
                self._height = size.height()
                self._friendly_name = window.title()

            case SourceType.AREA:

                # -- Ensure all values are provided
                if x is None or y is None or width is None or height is None:
                    log.error("x, y, width or height is None")
                    pass

                self._x = x
                self._y = y
                self._width = width
                self._height = height
                self._friendly_name = f"Area: {x}, {y}"

    def __str__(self) -> str:
        """
            Returns a string representation of the object.

            Returns:
                str: A string representation of the object.
        """
        return self._friendly_name if self._friendly_name is not None else "None"

    def get_window(self) -> QWindow | None:
        """
            Gets the window that is or has been selected.

            Returns:
                QWindow: The window that is or has been selected.
        """
        if self._window is None: log.warn("Window is None")
        return self._window

    def get_screen(self) -> QScreen:
        """
            Gets the screen that is or has been selected.

            Returns:
                QScreen: The screen that is or has been selected.
        """
        if self._screen is None: log.error("Screen is None")
        return self._screen
