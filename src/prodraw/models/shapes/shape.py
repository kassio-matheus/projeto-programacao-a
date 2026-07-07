from tkinter import *

from abc import *

from dataclasses import *


@dataclass
class Shape (ABC):
    """Abstract base class representing a generic drawable shape."""

    bg: StringVar

    start_x: float = None
    start_y: float = None
    end_x: float = None
    end_y: float = None

    # @property
    # # Retrieves the current background color string
    # def bg(self):
    #     return self._bg

    # @bg.setter
    # # Sets the background color by extracting the value from a StringVar
    # def bg(self, bg: StringVar):
    #     self._bg = bg.get()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def empty(self):
        pass
