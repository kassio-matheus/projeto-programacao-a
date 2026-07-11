from dataclasses import dataclass
from typing import ClassVar

from .shape import Shape


@dataclass
class Rectangle(Shape):
    """Represents a rectangle shape."""

    distance_x: float = None
    distance_y: float = None
    MIN_DISTANCE: ClassVar[float] = 2

    def start(self, x: float, y: float):
        self.start_x = x
        self.start_y = y

    def update(self, x: float, y: float):
        self.end_x = x
        self.end_y = y
        self.distance_x = abs((x - self.start_x))
        self.distance_y = abs((y - self.start_y))

    def has_min_size(self) -> bool:
        return self.distance_x is not None and self.distance_y is not None and self.distance_x > self.MIN_DISTANCE and self.distance_y > self.MIN_DISTANCE

    def to_tuple(self):
        return (self.start_x, self.start_y, self.end_x, self.end_y, self.distance_x, self.distance_y, self.bg)
