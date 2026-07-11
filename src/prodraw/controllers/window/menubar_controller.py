from prodraw.views.window import MenubarCommandView, MenubarCascadeView, MenubarView
from prodraw.models.window import MenubarCascade, MenubarCommand


class MenubarController:
    def __init__(self, root):
        self.root = root
        self.menubar = None
        self.view = MenubarView(self.root)

    def create(self):
        self.menubar = self.view.create()
        return self.menubar

    def add_command(self, model: MenubarCommand):
        command_view = MenubarCommandView(model=model)
        command_view.add_command(target_menu=self.menubar)

    def add_cascade(self, model: MenubarCascade):
        cascade_view = MenubarCascadeView(model=model)
        cascade_view.add_cascade(target_menu=self.menubar)

    def run(self):
        self.view.render(self.menubar)

    def destroy(self):
        self.view.destroy()
