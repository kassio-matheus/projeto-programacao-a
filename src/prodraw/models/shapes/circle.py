from dataclasses import dataclass
from typing import ClassVar

from prodraw.shapes import Shape


@dataclass
class Circle(Shape):
    """Represents a circle shape with a specific radius."""

    radius: float = None
    MIN_RADIUS: ClassVar[float] = 5

    def start(self, x: float, y: float):
        self.start_x = x
        self.start_y = y

    def update(self, x: float, y: float):
        self.end_x = x
        self.end_y = y
        self.radius = ((self.start_y - y) ** 2 + (self.start_x - x) ** 2) ** 0.5

    def has_min_size(self) -> bool:
        return self.radius is not None and self.radius > self.MIN_RADIUS

    def to_tuple(self):
        return (self.start_x, self.start_y, self.radius, self.bg)
