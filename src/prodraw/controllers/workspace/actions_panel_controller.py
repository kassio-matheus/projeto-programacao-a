from tkinter import Canvas
from prodraw.models.workspace.actions_panel_model import ActionsPanelModel
from prodraw.views.workspace.actions_panel_view import ActionsPanelView

from prodraw.controllers.workspace.cursor_controller import CursorController


class ActionsPanelController:
    """
    Connects the Actions Panel model and view.
    Acts as a bridge, delegating actions directly to the CursorController.
    """

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.model = ActionsPanelModel()
        self.view = ActionsPanelView(self.canvas, self.model)

        # Cursor is initialized as None and injected later via cross-reference in workspace.py
        self.cursor: CursorController = None

    def setup(self) -> None:
        """
        Builds the actions panel and establishes the initial state
        by binding the delegation methods to the view.
        """
        callbacks = {
            "undo": self._trigger_undo,
            "redo": self._trigger_redo,
            "delete": self._trigger_delete,
            "duplicate": self._trigger_duplicate,
            "layer_up": self._trigger_layer_up,
            "layer_down": self._trigger_layer_down
        }

        self.view.build(callbacks)

    def on_selection_change(self, is_selected: bool) -> None:
        """
        Called externally (by the Cursor) whenever a shape is selected or deselected.
        Updates the model and forces the view to refresh disabled/enabled states.
        """
        self.model.set_selection_state(is_selected)
        self.view.update_buttons_state()

    def _trigger_undo(self) -> None:
        # If Undo/Redo are handled globally or in a different controller, call it here
        print("Triggering Undo")

    def _trigger_redo(self) -> None:
        print("Triggering Redo")

    def _trigger_delete(self) -> None:
        if self.cursor:
            self.cursor.delete_selected_figures()

    def _trigger_duplicate(self) -> None:
        if self.cursor:
            self.cursor.copy_shapes()
            self.cursor.paste_shapes()

    def _trigger_layer_up(self) -> None:
        if self.cursor:
            self.cursor.raise_selected_figures()

    def _trigger_layer_down(self) -> None:
        if self.cursor:
            self.cursor.lower_selected_figures()