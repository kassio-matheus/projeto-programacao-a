from tkinter import Canvas, Frame
from prodraw.models.workspace.tool_options_model import ToolOptionsModel, PANEL_BG, SELECTED_BG, BUTTON_SIZE


class ToolOptionsView:
    """
    Renders the tool options panel containing fill, border, and size selectors.
    Uses Canvas shapes to draw the icons dynamically.
    """

    def __init__(self, canvas: Canvas, model: ToolOptionsModel):
        self.canvas = canvas
        self.model = model
        # Creates the main panel container with padding
        self.panel = Frame(canvas, bg=PANEL_BG, padx=31, pady=12)
        self.buttons = {}

    def build(self, on_fill_click, on_border_click, on_size_click) -> None:
        for col, fill_type in enumerate(self.model.fills):
            self._create_button(0, col, fill_type, "fill", on_fill_click)

        for col, border_type in enumerate(self.model.borders):
            self._create_button(1, col, border_type, "border", on_border_click)

        self.panel.place(relx=1.0, x=-16, y=160, anchor="ne")

    def _create_button(self, row: int, col: int, option_id: str, category: str, command) -> None:
        """Creates a single square button and draws the corresponding icon inside it."""
        btn_canvas = Canvas(self.panel, width=BUTTON_SIZE, height=BUTTON_SIZE,
                            bg=PANEL_BG, highlightthickness=0, cursor="hand2")
        btn_canvas.grid(row=row, column=col, padx=4, pady=4)

        self._draw_icon(btn_canvas, option_id, category)

        # Bind click action
        btn_canvas.bind("<Button-1>", lambda event,
                        opt=option_id, cmd=command: cmd(opt))

        self.model.canvas_by_option[option_id] = btn_canvas

        self.buttons[option_id] = {
            "canvas": btn_canvas,
            "category": category,
            "command": command
        }

    def _draw_icon(self, canvas: Canvas, option_id: str, category: str) -> None:
        """Draws the geometric representation of the tool inside the button."""
        # center = BUTTON_SIZE / 2
        padding = 6
        shape_size = BUTTON_SIZE - padding * 2

        stroke_color = "#ffffff"
        fill_color = "#5c5c66"  # Neutral gray for solid fills
        line_weight = 1.5

        if category == "fill":
            if option_id == "solid_border":
                canvas.create_rectangle(padding, padding, padding + shape_size, padding + shape_size,
                                        fill=fill_color, outline=stroke_color, width=line_weight, tags=("icon",))
            elif option_id == "solid_no_border":
                canvas.create_rectangle(padding, padding, padding + shape_size, padding + shape_size,
                                        fill=fill_color, width=0, tags=("icon",))
            elif option_id == "no_solid_border":
                canvas.create_rectangle(padding, padding, padding + shape_size, padding + shape_size,
                                        fill="", outline=stroke_color, width=line_weight, tags=("icon",))

        elif category == "border":
            if option_id == "solid":
                canvas.create_oval(padding, padding, padding + shape_size, padding + shape_size,
                                   outline=stroke_color, width=line_weight, tags=("icon",))
            elif option_id == "dotted":
                canvas.create_oval(padding, padding, padding + shape_size, padding + shape_size,
                                   outline=stroke_color, width=line_weight, dash=(2, 3), tags=("icon",))

    def highlight(self, option_id: str) -> None:
        """Applies the selection highlight to the specific option button."""
        if option_id in self.model.canvas_by_option:
            self.model.canvas_by_option[option_id].config(bg=SELECTED_BG)

    def unhighlight(self, option_id: str) -> None:
        """Removes the selection highlight from the specific option button."""
        if option_id in self.model.canvas_by_option:
            self.model.canvas_by_option[option_id].config(bg=PANEL_BG)

    def set_panel_state(self, state: str):
        """Desativa ou ativa visualmente todos os botões e os seus comportamentos."""
        if not hasattr(self, 'buttons') or not self.buttons:
            return

        outline_color = "#3a3a40" if state == "disabled" else "#ffffff"
        cursor = "arrow" if state == "disabled" else "hand2"

        for option_id, btn_data in self.buttons.items():
            btn = btn_data["canvas"]
            cmd = btn_data["command"]

            try:
                btn.config(cursor=cursor)
                btn.itemconfig("icon", outline=outline_color)

                if state == "disabled":
                    btn.unbind("<Button-1>")
                    self.unhighlight(option_id)

                    if btn.itemcget("icon", "fill") != "":
                        btn.itemconfig("icon", fill="#2a2a30")
                else:
                    if btn_data["category"] == "fill" and option_id in ("solid_border", "solid_no_border"):
                        btn.itemconfig("icon", fill="#5c5c66")

                    btn.bind("<Button-1>", lambda event,
                             opt=option_id, c=cmd: c(opt))
            except Exception as e:
                print(f"Error setting state on button '{option_id}': {e}")

    def set_border_buttons_state(self, state: str):
        """Desativa ou ativa especificamente os seletores de estilo de borda."""
        if not hasattr(self, 'buttons') or not self.buttons:
            return

        outline_color = "#3a3a40" if state == "disabled" else "#ffffff"
        cursor = "arrow" if state == "disabled" else "hand2"

        for option_id, btn_data in self.buttons.items():
            if btn_data["category"] != "border":
                continue

            btn = btn_data["canvas"]
            cmd = btn_data["command"]

            try:
                btn.config(cursor=cursor)
                btn.itemconfig("icon", outline=outline_color)

                if state == "disabled":
                    btn.unbind("<Button-1>")
                    self.unhighlight(option_id)
                else:
                    btn.bind("<Button-1>", lambda event,
                             opt=option_id, c=cmd: c(opt))
            except Exception as e:
                print(
                    f"Error setting state on border button '{option_id}': {e}")
