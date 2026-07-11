# from prodraw.window import FullScreen, Version
from prodraw.controllers import create_window
from prodraw.models import Version
from prodraw.workspace import Workspace


def main():
    window = create_window(title="ProDraw", is_fullscreen=True,
                           icon="public/icons/logo_icon.png")
    version = Version("1.0.0")

    Workspace(root=window.view.root, version=version, window=window).start()

    window.run()  # last command in the scope -> required


main()
