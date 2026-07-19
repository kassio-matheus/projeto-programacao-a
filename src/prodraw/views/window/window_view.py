import tkinter as tk
from dataclasses import dataclass


@dataclass
class WindowView:
    """Create the window view on Tkinter"""
    _root = tk.Tk()

    @property
    def root(self):
        return self._root

    def set_title(self, title: str):
        self._root.title(title)

    def set_size(self, width: int, height: int):
        self._root.geometry(f"{width}x{height}")

    def set_fullscreen(self, enabled: bool):
        self._root.attributes("-fullscreen", enabled)

    def set_app_icon(self, icon: str):
        photo = tk.PhotoImage(file=icon)
        self._root.wm_iconphoto(True, photo)

    def start(self):
        self._root.mainloop()

    def destroy(self):
        self._root.destroy()
        self._root = None
