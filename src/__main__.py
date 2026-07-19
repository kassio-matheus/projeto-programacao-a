from prodraw.controllers import create_window
from prodraw.workspace import Workspace


def main():
    #Create default window in full screen
    window = create_window(title="ProDraw", is_fullscreen=True,
                           icon="public/icons/logo_icon.png")

    #Create default workspace
    Workspace(root=window.view.root, window=window).start()

    window.run()  # last command in the scope -> required


if __name__ == "__main__":
    main()
