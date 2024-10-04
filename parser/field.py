from enum import Enum

class FieldType(Enum):
    MINUTE = 1
    HOUR = 2
    DAY_OF_MONTH = 3
    MONTH = 4
    DAY_OF_WEEK = 5


class Field:
    def __init__(self, min_value, max_value, name = "") -> None:
        self.min_value = min_value
        self.max_value = max_value
        self.name = name

    def generate_range(self, start: int, end: int, interval = 1) -> str:
        if start < self.min_value or start > self.max_value or interval > self.max_value:
            raise ValueError(f"Start {start} or interval {interval} is out of range of the field values {self.min_value} and {self.max_value}")
        values = list(range(start, end+1, interval))
        return " ".join(str(val) for val in values)

    def parse(self, expression: str) -> str:
        if expression.isnumeric():
            return expression
        
        elif expression == "*":
            return self.generate_range(self.min_value, self.max_value)
        
        elif expression.__contains__(","):
            sub_expressions = expression.split(",")
            concat_expr = []
            for expr in sub_expressions:
                concat_expr.append(self.parse(expr))
            return " ".join(val for val in concat_expr)
        
        elif expression.__contains__("/"):
            if len(expression.split("/")) != 2:
                raise ValueError(f"Invalid expression {expression}")
            start, interval = map(str, expression.split("/"))
            range_start = int(start) if start.isnumeric() else self.min_value
            return self.generate_range(range_start, self.max_value, int(interval))
        
        elif expression.__contains__("-"):
            if len(expression.split("-")) != 2:
                raise ValueError(f"Invalid expression {expression}")
            start, end = map(int, expression.split("-"))
            return self.generate_range(start, end)
        
        else:
            raise ValueError(f"Unsupported expression: {expression}")
        
        
    