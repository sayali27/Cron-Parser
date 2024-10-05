from parser.field import FieldType
from parser.output import output_values
from parser.factory import factory
from collections import OrderedDict

def parse_expression(regex: str):
    tokens = regex.split(' ')
    parsed_fields = OrderedDict()

    if len(tokens) - 1 != len(FieldType):
        raise ValueError(f"Expression size does not match the size of supported fields {len(FieldType)}")
    
    for i, expression in enumerate(tokens[:-1]):
        field = factory.get_field(FieldType(i+1))
        times = field.parse(expression)
        parsed_fields[field.name] = times

    parsed_fields["command"] =  tokens[-1]
    return parsed_fields

    
