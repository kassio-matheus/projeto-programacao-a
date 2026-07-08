from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Shape(ABC):
    """Abstract base class representing a generic drawable shape."""

    bg: str

    start_x: float = None
    start_y: float = None
    end_x: float = None
    end_y: float = None

    @abstractmethod
    def start(self, x: float, y: float):
        pass

    @abstractmethod
    def update(self, x: float, y: float):
        pass

    @abstractmethod
    def has_min_size(self) -> bool:
        """Check the min size of shape to create"""
        pass

    @abstractmethod
    def to_tuple(self):
        """Snapshot of shape"""
        pass
