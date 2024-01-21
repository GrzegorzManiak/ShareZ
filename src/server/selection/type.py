from enum import Enum



class SourceType(Enum):
    """
        The type of source that is or has been selected.
    """

    SCREEN = 0
    WINDOW = 1
    AREA = 2

    def __str__(self):
        return self.name
    


class CaptureType(Enum):
    """
        The type of capture that is about to occure.
    """

    VIDEO = 0
    IMAGE = 1

    def __str__(self):
        return self.name