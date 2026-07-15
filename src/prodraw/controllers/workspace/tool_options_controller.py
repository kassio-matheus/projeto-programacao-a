from tkinter import Canvas
from prodraw.models.workspace.tool_options_model import ToolOptionsModel
from prodraw.views.workspace.tool_options_view import ToolOptionsView


class ToolOptionsController:
    """
    Connects the Tool Options model and view. 
    Handles user selections for fills, borders, and sizes.
    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.model = ToolOptionsModel()
        self.view = ToolOptionsView(self.canvas, self.model)

    def setup(self) -> None:
        """Builds the options panel and sets the default highlights."""
        self.view.build(
            on_fill_click=self._on_fill_select,
            on_border_click=self._on_border_select,
            on_size_click=self._on_size_select
        )

        # Highlight default options loaded from the model
        initial_fill = self.model.get_fill()
        initial_border = self.model.get_border()

        self.view.highlight(initial_fill)

        # If the default fill doesn't allow border, start with borders disabled
        if initial_fill == "solid_no_border":
            self.view.set_border_buttons_state("disabled")
        else:
            self.view.highlight(initial_border)

    def _on_fill_select(self, fill_option: str) -> None:
        old_fill = self.model.get_fill()

        self.view.unhighlight(old_fill)
        self.view.highlight(fill_option)
        self.model.set_fill(fill_option)

        if fill_option == "solid_no_border":
            self.view.set_border_buttons_state("disabled")
        else:
            self.view.set_border_buttons_state("normal")
            self.view.highlight(self.model.get_border())

        # 2. DISPARE O CALLBACK AQUI informando a mudança de preenchimento
        if self.on_option_change_callback:
            self.on_option_change_callback(fill_option, "fill")

    def _on_border_select(self, border_option: str) -> None:
        old_border = self.model.get_border()

        self.view.unhighlight(old_border)
        self.view.highlight(border_option)
        self.model.set_border(border_option)

        # 3. DISPARE O CALLBACK AQUI informando a mudança de borda
        if self.on_option_change_callback:
            self.on_option_change_callback(border_option, "border")

    def _on_size_select(self, size_option: str) -> None:
        """Placeholder for size option selector if implemented in the future."""
        pass

    def sync_ui_from_shape(self, fill_option_id: str, border_option_id: str, is_disabled: bool = False) -> None:
        """
        Synchronizes the Tool Options UI highlighting with the properties 
        of the currently selected shape.
        """
        if is_disabled:
            # Blocks and disables all interaction with the panel
            self.view.set_panel_state("disabled")
            return

        # Ensure everything is active and normal first
        self.view.set_panel_state("normal")

        # 1. Update Fill highlight in Model and View
        old_fill = self.model.get_fill()
        self.view.unhighlight(old_fill)
        self.model.set_fill(fill_option_id)
        self.view.highlight(fill_option_id)

        # 2. Update Border highlight in Model and View
        old_border = self.model.get_border()
        self.view.unhighlight(old_border)
        self.model.set_border(border_option_id)
        self.view.highlight(border_option_id)

        # 3. Handle disabling/enabling of border buttons based on fill type
        if fill_option_id == "solid_no_border":
            self.view.set_border_buttons_state("disabled")
        else:
            self.view.set_border_buttons_state("normal")

    def disable_options(self) -> None:
        """Disables the entire options panel (For Lines, FreeDraw, Cursor)."""
        self.view.set_panel_state("disabled")

    def enable_options(self) -> None:
        """Re-enables the panel (For Rectangles, Squares, Circles, Ovals)."""
        self.view.set_panel_state("normal")

        # Restore active states and highlights based on current Model memory
        active_fill = self.model.get_fill()
        self.view.highlight(active_fill)

        if active_fill == "solid_no_border":
            self.view.set_border_buttons_state("disabled")
        else:
            self.view.set_border_buttons_state("normal")
            self.view.highlight(self.model.get_border())
