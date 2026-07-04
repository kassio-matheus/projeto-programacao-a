from .window import Window


class FullScreen(Window):
    def __init__(self, title):
        super().__init__(title, is_fullscreen=True)
        self.root.attributes("-fullscreen", True)

    # Toggles the window fullscreen mode - SOLID
    def toggle(self, event=None):
        is_fullscreen = not self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", is_fullscreen)

    # Exits the window fullscreen mode - SOLID
    def exit(self, event=None):
        self.root.attributes("-fullscreen", False)

    def bind(self):
        self.root.bind("<F11>", self.toggle)
        self.root.bind("<Escape>", self.exit)
        return self
