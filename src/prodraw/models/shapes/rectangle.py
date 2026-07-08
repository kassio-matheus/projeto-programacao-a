from dataclasses import dataclass
from typing import ClassVar

from prodraw.shapes import Shape


@dataclass
class Rectangle(Shape):
    """Represents a rectangle shape."""

    distance: float = None
    MIN_DISTANCE: ClassVar[float] = 5

    def start(self, x: float, y: float):
        self.start_x = x
        self.start_y = y

    def update(self, x: float, y: float):
        self.end_x = x
        self.end_y = y
        self.distance = abs((x - self.start_x)) + abs((y - self.start_y))

    def has_min_size(self) -> bool:
        return self.distance is not None and self.distance >= self.MIN_DISTANCE

    def to_tuple(self):
        return (self.start_x, self.start_y, self.end_x, self.end_y, self.distance, self.bg)
