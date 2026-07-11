from typing import Callable

from prodraw.models import Window
from prodraw.views import WindowView

from .menubar_controller import MenubarController
from prodraw.models.window.menubar import MenubarCascade, MenubarCommand


class WindowController:
    def __init__(self):
        self.view = WindowView()
        self.current: Window = None
        self.menu = [
            {"Arquivo": {"Sair": lambda: self.destroy()}},
            {"Visualização": {}},
            {"Ajuda": {}},
        ]

    def load(self, title: str = "ProDraw", is_fullscreen: bool = True, icon: str = ""):
        self.current = Window(title=title, is_fullscreen=is_fullscreen)

        self.view.set_fullscreen(enabled=True)
        self.view.set_title(title)

        if (len(icon) > 0):
            self.view.set_app_icon(icon)

    def toggle(self, event=None):
        is_fullscreen = not self.view.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", is_fullscreen)

    def exit(self, event=None):
        self.view.root.attributes("-fullscreen", False)

    def bind(self, keyword: str, command: Callable):
        self.view.root.bind(keyword, command)

        return self

    def create_menubar(self):
        self.main_menubar = MenubarController(self.view.root)
        self.main_menubar.create()

        for submenu in self.menu:
            name_submenu = next(iter(submenu.keys()))

            submenubar = MenubarController(root=self.main_menubar.menubar)
            submenubar.create()

            cascade = MenubarCascade(
                name_submenu, menu=submenubar.menubar, underline=0)
            self.main_menubar.add_cascade(cascade)

            for label, command in submenu[name_submenu].items():
                item = MenubarCommand(label, command=command)
                submenubar.add_command(item)

        self.main_menubar.run()

    def update_menu(self, isCascade: bool = False, isSubItem: bool = False, subItem: str = "", label: str = "", command: Callable = None):
        if isSubItem and subItem:
            for submenu in self.menu:
                if subItem in submenu:
                    submenu[subItem] = {label: command, **submenu[subItem]}
                    break
        elif isCascade:
            if not any(label in submenu for submenu in self.menu):
                self.menu.insert(0, {label: {}})
        else:
            pass

        self.main_menubar.destroy()
        self.create_menubar()

    def run(self):
        self.view.start()
        pass

    def destroy(self):
        self.view.destroy()
        pass
