from tkinter import Canvas, Frame, PhotoImage

# Importing SELECTED_BG to use as the "hover" color
from prodraw.models.workspace.actions_panel_model import ActionsPanelModel, PANEL_BG, SELECTED_BG, BUTTON_SIZE


class ActionsPanelView:
    """
    Renders the actions panel containing undo, redo, delete, duplicate, and layer controls.
    Uses PhotoImage to render real image icons and swaps to a disabled state icon when unavailable.
    """

    def __init__(self, canvas: Canvas, model: ActionsPanelModel):
        self.canvas = canvas
        self.model = model

        self.panel = Frame(canvas, bg=PANEL_BG, padx=12, pady=12)
        self.buttons = {}

    def build(self, callbacks: dict) -> None:
        """Iterates through the model's actions and builds the UI buttons in two rows."""
        for index, action_id in enumerate(self.model.actions):
            if index < 4:
                row = 0
                col = index
            else:
                row = 1
                col = index - 4

            self._create_button(row, col, action_id, callbacks.get(action_id))

        self.panel.place(relx=1.0, x=-16, y=267, anchor="ne")
        self.update_buttons_state()

    def _create_button(self, row: int, col: int, action_id: str, command) -> None:
        """Creates a single square button and loads the corresponding active and disabled PhotoImages."""
        btn_canvas = Canvas(self.panel, width=BUTTON_SIZE, height=BUTTON_SIZE,
                            bg=PANEL_BG, highlightthickness=0, cursor="hand2")
        btn_canvas.grid(row=row, column=col, padx=4, pady=4)

        active_icon = None
        disabled_icon = None

        try:
            # Load the normal active image
            active_icon = PhotoImage(file=f"public/icons/{action_id}.png")

            # Load the image with the 'disabled_' prefix
            try:
                disabled_icon = PhotoImage(
                    file=f"public/icons/disabled_{action_id}.png")
            except Exception as e:
                print(
                    f"Disabled icon missing for {action_id}, falling back to active icon. ({e})")
                disabled_icon = active_icon

            # Draw the active image initially in the center of the canvas
            center_x = BUTTON_SIZE / 2
            center_y = BUTTON_SIZE / 2
            btn_canvas.create_image(
                center_x, center_y, image=active_icon, tags=("icon",))

        except Exception as e:
            print(f"Failed to load base icon for {action_id}: {e}")

        # Bind hover events
        btn_canvas.bind("<Enter>", lambda event, btn=btn_canvas,
                        a_id=action_id: self._on_hover_enter(event, btn, a_id))
        btn_canvas.bind("<Leave>", lambda event,
                        btn=btn_canvas: self._on_hover_leave(event, btn))

        # Save references in the dictionary for access in update_buttons_state and to prevent Garbage Collection
        self.buttons[action_id] = {
            "canvas": btn_canvas,
            "command": command,
            "active_icon": active_icon,
            "disabled_icon": disabled_icon
        }

    def _on_hover_enter(self, event, btn: Canvas, action_id: str) -> None:
        """Applies the hover background color if the button is currently active."""
        # is_active = (action_id in ["undo", "redo"]
        #              ) or self.model.get_selection_state()
        # if is_active:
        #     btn.config(bg=SELECTED_BG)
        pass

    def _on_hover_leave(self, event, btn: Canvas) -> None:
        """Restores the default background color when the mouse leaves."""
        btn.config(bg=PANEL_BG)

    def update_buttons_state(self) -> None:
        """
        Disables or enables buttons based on the model's selection state.
        Swaps the icon image to the disabled state when unavailable.
        """
        if not hasattr(self, 'buttons') or not self.buttons:
            return

        has_selection = self.model.get_selection_state()
        always_active = ["undo", "redo"]

        for action_id, btn_data in self.buttons.items():
            btn = btn_data["canvas"]
            cmd = btn_data["command"]
            active_icon = btn_data["active_icon"]
            disabled_icon = btn_data["disabled_icon"]

            is_active = (action_id in always_active) or has_selection
            cursor = "hand2" if is_active else "arrow"

            try:
                btn.config(cursor=cursor)

                if not is_active:
                    # Disable interactions, reset background color, and swap to the disabled icon
                    btn.unbind("<Button-1>")
                    btn.config(bg=PANEL_BG)
                    if disabled_icon:
                        btn.itemconfig("icon", image=disabled_icon)
                else:
                    # Enable interactions and revert to the original active icon
                    if cmd:
                        btn.bind("<Button-1>", lambda event, c=cmd: c())
                    if active_icon:
                        btn.itemconfig("icon", image=active_icon)
            except Exception as e:
                print(
                    f"Error updating state on action button '{action_id}': {e}")
