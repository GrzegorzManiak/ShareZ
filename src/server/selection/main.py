from src.logger import log
from PySide6.QtGui import QGuiApplication, QScreen, QWindow
from src.server.display_server.main import DisplayServerManager
from src.server.selection.selection import Selection
from src.server.selection.type import SourceType, CaptureType



def get_all_screens(
    capture: CaptureType = CaptureType.IMAGE,
) -> list[Selection]:
    """
        Gets all screens that are connected to the computer.

        Args:
            capture (CaptureType): The type of capture that is about to occure.
                                   default: CaptureType.IMAGE

        Returns:
            List[Selection]: A list of all screens that are connected to the computer.
    """
    log.info("Getting all screens")
    screens = QGuiApplication.screens()

    # -- Create a list of Selection objects
    selection_list = []
    for screen in screens:
        selection_list.append(Selection(
            source=SourceType.SCREEN,
            capture=capture,
            screen=screen,
        ))
    
    return selection_list