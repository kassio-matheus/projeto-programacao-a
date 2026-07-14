from dataclasses import *
from tkinter import *

from typing import Callable, Any
from abc import ABC, abstractmethod


@dataclass
class Tools(ABC):
    canvas: Canvas = None
    figures: dict = None
    get_bg: Callable[[], str] = None
    view: Any = None
    window: Callable = None

    @abstractmethod
    def _on_press(self, event: Event):
        pass

    @abstractmethod
    def _on_drag(self, event: Event):
        pass

    @abstractmethod
    def _on_release(self, event: Event):
        pass
