class CursorModel:
    """Holds cursor configuration data."""

    def __init__(self):
        self.outline_color = "#5B5B5B"

    def start(self, x: float, y: float):
        self.start_x = x
        self.start_y = y

        self.end_x = x
        self.end_y = y

    def update(self, x: float, y: float):
        self.end_x = x
        self.end_y = y

    def has_min_size(self) -> bool:
        return True

    def to_tuple(self):
        return (self.start_x, self.start_y, self.end_x, self.end_y)
