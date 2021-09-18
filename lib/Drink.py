from dataclasses import dataclass
import Liquid


@dataclass
class Drink:

    name: str
    quantities: Liquid
    img_source: str

    def __str__(self):
        return self.name
