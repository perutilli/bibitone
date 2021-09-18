from dataclasses import dataclass


@dataclass
class Liquid:

    name: str
    position: list(int)
    shot: bool  # is shottable

    def __str__(self):
        return self.name
