from enum import Enum


class DisplayServerType(Enum):
    """
        An enum that represents the type of display server.
    """
    UNKNOWN = -1
    X11 = 0
    WAYLAND = 1

    def __str__(self):
        return self.name
    


class DesktopEnvironmentType(Enum):
    """
        An enum that represents the type of desktop environment.
        I can only test this on Gnome, so if anyone wants to test
        this on other desktop environments, please do.
    """
    UNKNOWN = -1
    GNOME = 0

    def __str__(self):
        return self.name