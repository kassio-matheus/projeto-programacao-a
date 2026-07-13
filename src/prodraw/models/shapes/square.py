from dataclasses import dataclass
from typing import ClassVar

from .shape import Shape


@dataclass
class Square(Shape):
    """Represents a square shape."""

    distance_x: float = None
    MIN_DISTANCE: ClassVar[float] = 5

    def start(self, x: float, y: float):
        self.start_x = x
        self.start_y = y

    def update(self, x: float):

        self.distance_x = abs((x - self.start_x))

        self.end_x = self.distance_x+self.start_x
        self.end_y = self.distance_x+self.start_y

    def has_min_size(self) -> bool:
        return self.distance_x is not None and self.distance_x > self.MIN_DISTANCE

    def to_tuple(self):
        return (self.shape_id, self.start_x, self.start_y, self.end_x, self.end_y, self.distance_x, self.bg)
