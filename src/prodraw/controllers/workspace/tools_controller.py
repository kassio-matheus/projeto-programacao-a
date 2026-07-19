from tkinter import Canvas, StringVar

# Models
from prodraw.models.workspace.tools_model import ToolsModel, DEFAULT_TOOL
from prodraw.views.workspace.toolbar_view import ToolbarView
from prodraw.models.workspace.toolbar_model import ToolbarModel

from prodraw.models.workspace.buttons_model.rectangle import Rectangle
from prodraw.models.workspace.buttons_model.circle import Circle
from prodraw.models.workspace.buttons_model.oval import Oval
from prodraw.models.workspace.buttons_model.line import Line
from prodraw.models.workspace.buttons_model.freedraw import FreeDraw
from prodraw.models.workspace.buttons_model.cursor import Cursor
from prodraw.models.workspace.buttons_model.square import Square

# Controllers
from prodraw.controllers.shapes.shape_controller import ShapeController
from prodraw.controllers.window import WindowController


class ToolsController:
    """Manages the toolbar UI and activates drawing tools on selection."""

    # Maps each tool key to its button class
    BUTTON_CLASSES = {
        'cursor': Cursor,
        'rectangle': Rectangle,
        'square': Square,
        'circle':    Circle,
        'oval':      Oval,
        'line':      Line,
        'freedraw':  FreeDraw
    }

    def __init__(self, canvas: Canvas, selected_color_var: StringVar, figures: dict, window: WindowController):
        self.canvas = canvas
        self.selected_color_var = selected_color_var
        self.figures = figures
        self.model = ToolsModel()
        self.toolbar_model = ToolbarModel()
        self.view = ToolbarView(canvas, self.toolbar_model)
        self.window = window

        cursor_tool = self.model.tools.get("cursor")
        self._cursor = cursor_tool[0] if cursor_tool else None

    @property
    def cursor(self):
        """Retorna o controlador do cursor."""
        return self._cursor

    def setup(self):
        """Build the toolbar and activate the default tool."""
        self.view.build()

        for key, btn_cls in self.BUTTON_CLASSES.items():
            self.view.create_tool_button(
                tool_cls=btn_cls,
                selected_color_var=self.selected_color_var,
                selected_option=self.model.selected_option,
                selected_key=key,
                on_click=self._on_select,
            )

        cursor_tool = self.model.tools.get("cursor")
        if cursor_tool:
            bind_fn, view_fn = cursor_tool[0], cursor_tool[1]
            bind_fn.canvas = self.canvas
            bind_fn.window = self.window
            view_fn.canvas = self.canvas
            bind_fn.view = view_fn
            bind_fn.figures = self.figures
            bind_fn.get_bg = self.selected_color_var.get

            bind_fn.tool_options_model = getattr(
                self, 'tool_options_model', None)

            bind_fn.selected_color_var = self.selected_color_var

            bind_fn.setup()

        self._on_select(DEFAULT_TOOL)

    def _on_select(self, tool_key: str):
        """Unbind the previous tool and bind the newly selected one."""

        self.model.selected_option.set(tool_key)
        bind_fn = self.model.tools.get(tool_key)[0]
        view_fn = self.model.tools.get(tool_key)[1]

        bind_fn.canvas = self.canvas
        view_fn.canvas = self.canvas

        bind_fn.view = view_fn

        bind_fn.figures = self.figures
        bind_fn.get_bg = self.selected_color_var.get

        bind_fn.selected_color_var = self.selected_color_var

        bind_fn.tool_options_model = getattr(self, 'tool_options_model', None)

        ShapeController(bind_fn, view_fn)

        if (tool_key == "cursor"):
            self._cursor = bind_fn

        tool_options_ctrl = getattr(self, 'tool_options_controller', None)
        if tool_options_ctrl:
            if tool_key in ('line', 'freedraw', 'cursor'):
                tool_options_ctrl.disable_options()
            else:
                tool_options_ctrl.enable_options()
