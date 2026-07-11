from tkinter import Canvas, StringVar
from prodraw.models.workspace.tools_model import ToolsModel, DEFAULT_TOOL
from prodraw.views.workspace.toolbar_view import ToolbarView
from prodraw.models.workspace.toolbar_model import ToolbarModel

from prodraw.models.workspace.buttons_model.rectangle import Rectangle
from prodraw.models.workspace.buttons_model.circle import Circle
from prodraw.models.workspace.buttons_model.oval import Oval
from prodraw.models.workspace.buttons_model.line import Line
from prodraw.models.workspace.buttons_model.freedraw import FreeDraw


class ToolsController:
    """Manages the toolbar UI and activates drawing tools on selection."""

    # Maps each tool key to its button class
    BUTTON_CLASSES = {
        'rectangle': Rectangle,
        'circle':    Circle,
        'oval':      Oval,
        'line':      Line,
        'freedraw':  FreeDraw,
        'square': Rectangle
    }

    def __init__(self, canvas: Canvas, selected_color_var: StringVar, figures: dict):
        self.canvas = canvas
        self.selected_color_var = selected_color_var
        self.figures = figures
        self.model = ToolsModel()
        self.toolbar_model = ToolbarModel()
        self.view = ToolbarView(canvas, self.toolbar_model)

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

        # Activate the default tool immediately
        self._on_select(DEFAULT_TOOL)

    def _on_select(self, tool_key: str):
        """Unbind the previous tool and bind the newly selected one."""
        # Unbind the previous controller if one exists
        self.model.selected_option.set(tool_key)
        bind_fn = self.model.tools.get(tool_key)
        if bind_fn:
            self.model.active_controller = bind_fn(
                canvas=self.canvas,
                figures=self.figures,
                bg=self.selected_color_var,
            )
