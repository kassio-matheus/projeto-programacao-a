# Styling constants matching the existing panels
PANEL_BG = "#1c1c22"
SELECTED_BG = "#3a3a42"
BUTTON_SIZE = 30 

class ActionsPanelModel:
    """
    Holds the state for the actions panel.
    Tracks whether a figure is currently selected to determine button availability.
    """

    def __init__(self):
        # Define available action buttons mapped to unique string identifiers
        self.actions = [
            "undo", 
            "redo", 
            "delete", 
            "duplicate", 
            "layer_up", 
            "layer_down"
        ]

        # State tracking for UI logic
        self.has_selection = False

    def set_selection_state(self, state: bool) -> None:
        """Updates the current selection state (True if a figure is selected)."""
        self.has_selection = state

    def get_selection_state(self) -> bool:
        """Returns the current selection state."""
        return self.has_selection