from dataclasses import dataclass

from .shape import Shape


@dataclass
class FreeDraw(Shape):
    """Represents a free draw shape."""

    def start(self, x: float, y: float):
        self.start_x = x
        self.start_y = y

    def update(self, x: float, y: float):
        self.end_x = x
        self.end_y = y

    def has_min_size(self) -> bool:
        return True

    def to_tuple(self):
        return (self.shape_id, self.start_x, self.start_y, self.end_x, self.end_y, self.bg)
