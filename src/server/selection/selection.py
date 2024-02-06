from logger import log
from PySide6.QtGui import QScreen, QWindow
from server.selection.type import SourceType, CaptureType


class Selection:
    _source: SourceType
    _screen: QScreen
    _window: QWindow | None
    _friendly_name: str | None = None

    _x: int = 0
    _y: int = 0
    _z: int = 0

    _width: int = 0
    _height: int = 0

    def __init__(self,
                 source: SourceType,

                 screen: QScreen | None = None,
                 window: QWindow | None = None,

                 x: int | None = None,
                 y: int | None = None,
                 width: int | None = None,
                 height: int | None = None,

                 z: int | None = None,

                 friendly_name: str | None = None,
                 ):
        """
            Creates a new Area object.

            Args:
                source (SourceType): The type of source that is or has been selected.
                screen (QScreen): The screen that is or has been selected.
                window (QWindow): The window that is or has been selected.
                x (int): The x position of the area.
                y (int): The y position of the area.
                z (int): The z index of the area (E.g. The window level).
                width (int): The width of the area.
                height (int): The height of the area.
        """

        self._type = source
        self._z = z

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
                self._screen = screen

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
                self._window = window

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

        # -- Set the friendly name (If provided, overrides the default)
        self._friendly_name = friendly_name

    def __str__(self) -> str:
        """
            Returns a string representation of the object.

            Returns:
                str: A string representation of the object.
        """
        return self._friendly_name if self._friendly_name is not None else "None"

    def get_name(self) -> str:
        """
            Gets the name of the object.

            Returns:
                str: The name of the object.
        """
        return self._friendly_name if self._friendly_name is not None else "None"

    def set_friendly_name(self, name: str) -> None:
        """
            Sets the friendly name of the object.

            Args:
                name (str): The friendly name of the object.
        """
        self._friendly_name = name

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

    def get_size(self) -> tuple[int, int]:
        """
            Gets the size of the area.

            Returns:
                tuple[int, int]: The size of the area.
        """
        return self._width, self._height

    def get_position(self) -> tuple[int, int]:
        """
            Gets the position of the area.

            Returns:
                tuple[int, int]: The position of the area.
        """
        return self._x, self._y