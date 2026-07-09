class TextVersionModel:
    """Holds version string and label style data."""

    def __init__(self, version: str):
        self.version = version
        self.text = f"ProDraw @{version}"
        self.fg = "#3F3F3F"
        self.bg = "#101010"
        self.font = ("Helvetica", 12, "bold")
