from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    value: str

    def __str__(self):
        return self.value
