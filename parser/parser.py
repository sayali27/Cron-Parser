from parser.field import FieldType
from parser.parser_utils import parse_day_of_month, parse_hours, parse_minutes
from parser.factory import factory


def parse_expression(regex: str):
    print(f"{regex}")
    tokens = regex.split(' ')

    print(f"fieldtype 1 {FieldType(1)}")

    for i, expression in enumerate(tokens[:-1]):
        field = factory.get_field(FieldType(i+1))
        output = field.parse(expression)
        print(output)
    

    
