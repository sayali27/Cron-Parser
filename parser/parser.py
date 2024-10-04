from parser.field import FieldType
from parser.output import output_values
from parser.factory import factory


def parse_expression(regex: str):
    tokens = regex.split(' ')
    
    for i, expression in enumerate(tokens[:-1]):
        field = factory.get_field(FieldType(i+1))
        times = field.parse(expression)
        output_values(field.name, times)
    output_values("command", tokens[-1])

    
