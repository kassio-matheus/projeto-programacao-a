import tkinter as tk

from abc import ABC, abstractmethod


class Window(ABC):
    def __init__(self, title, is_fullscreen, width=800, height=600):
        super().__init__()
        self.root = tk.Tk()
        self.root.title(title)

        if not is_fullscreen:
            self.root.geometry(f"{width}x{height}")

        self.is_fullscreen = is_fullscreen

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, new_root):
        self._root = new_root

    @abstractmethod
    def bind(self):
        pass