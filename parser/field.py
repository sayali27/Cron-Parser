from enum import Enum

class FieldType(Enum):
    MINUTE = 1
    HOUR = 2
    DAY_OF_MONTH = 3

class Field:
    def __init__(self, min_value, max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def parse(self, expression: str):
        return (f"hello + {self.min_value}   {self.max_value}")