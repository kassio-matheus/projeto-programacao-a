from prodraw.window import FullScreen, Version
from prodraw.workspace import Workspace


class App:
    def __init__(self):
        pass

    def run(self):
        version = Version("1.0.0")
        window = FullScreen(title="ProDraw")
        window.bind()

        Workspace(root=window.root, version=version).start()

        window.root.mainloop()
