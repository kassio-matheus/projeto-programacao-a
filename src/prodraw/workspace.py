from tkinter import Canvas, Tk

from prodraw.controllers.workspace.color_picker_controller import ColorPickerController
from prodraw.controllers.workspace.grids_controller import GridsController
from prodraw.controllers.workspace.text_version_controller import TextVersionController
from prodraw.controllers.workspace.clear_draws_controller import ClearDrawsController
from prodraw.controllers.workspace.tools_controller import ToolsController
from prodraw.controllers.workspace.zoom_controller import ZoomController


class Workspace:
    """Main workspace — wires up all MVC components."""

    def __init__(self, root: Tk, version):
        self.root = root
        self.canvas = Canvas(root, bg='#101010', highlightthickness=0,
                             relief="flat", borderwidth=0)
        # figures dict matches the shape keys used by shape controllers
        self.figures = {
            'Circle': [], 'Rectangle': [],
            'Oval': [], 'Line': [], 'FreeDraw': []
        }
        self.version = version

    def start(self):
        self.canvas.pack(fill="both", expand=True)

        # Version watermark at the bottom-left
        TextVersionController(self.canvas, self.version).setup()

        # Dot grid — redraws on every canvas resize
        grid_ctrl = GridsController(self.canvas, self.version)
        self.canvas.bind("<Configure>", grid_ctrl.on_resize)

        # Color picker — returns the active color StringVar
        color_ctrl = ColorPickerController(self.canvas)
        selected_color_var = color_ctrl.setup()

        # Clear-all button
        ClearDrawsController(self.canvas, self.figures).setup()

        # Toolbar with drawing tool buttons
        ToolsController(self.canvas, selected_color_var, self.figures).setup()

        # Scroll-to-zoom
        zoom_ctrl = ZoomController(self.canvas)
        self.canvas.bind("<MouseWheel>", zoom_ctrl.on_scroll)