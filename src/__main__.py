from prodraw.controllers import create_window
from prodraw.workspace import Workspace


def main():
    #Create default window in full screen
    window = create_window(title="ProDraw", is_fullscreen=True,
                           icon="public/icons/logo_icon.png")
<<<<<<< HEAD:src/__main__.py
=======
    version = Version("1.0.5")
>>>>>>> 0a803038fde344ee9180a8af1457d668244fce68:src/main.py

    #Create default workspace
    Workspace(root=window.view.root, window=window).start()

    window.run()  # last command in the scope -> required


if __name__ == "__main__":
    main()
