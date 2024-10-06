from parser.constants import COMMAND_FIELD_NAME
from parser.field import FieldType
from parser.output import output_values
from parser.factory import factory
from collections import OrderedDict

def parse_expression(regex: str):
    tokens = regex.split(' ')
    parsed_fields = OrderedDict()

    if len(tokens) - 1 != len(FieldType):
        raise SyntaxError(f"Expression size does not match the size of supported time fields {len(FieldType)}")
    
    for i, expression in enumerate(tokens[:-1]):
        field = factory.get_field(FieldType(i+1))
        schedule = field.parse(expression)
        parsed_fields[field.name] = schedule

    # add the command after the schedule for all other fields is added
    parsed_fields[COMMAND_FIELD_NAME] =  tokens[-1]
    return parsed_fields

    
