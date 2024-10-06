import pytest
import json

from parser.parser import parse_expression
from parser.constants import *

test_data = [
    ("*/15 1,5 1-3,7 5 * pwd", 
     [
        f"{MINUTES_FIELD_NAME}: 0 15 30 45",
        f"{HOURS_FIELD_NAME}: 1 5",
        f"{DAY_OF_MONTH_FIELD_NAME}: 1 2 3 7",
        f"{MONTHS_FIELD_NAME}: 5",
        f"{DAY_OF_WEEK_FIELD_NAME}: 1 2 3 4 5 6 7",
        f"{COMMAND_FIELD_NAME}: pwd",
    ]
    ),
    ("20 1,5,9 1-3,7 5 1-2 pwd", 
     [
        f"{MINUTES_FIELD_NAME}: 20",
        f"{HOURS_FIELD_NAME}: 1 5 9",
        f"{DAY_OF_MONTH_FIELD_NAME}: 1 2 3 7",
        f"{MONTHS_FIELD_NAME}: 5",
        f"{DAY_OF_WEEK_FIELD_NAME}: 1 2",
        f"{COMMAND_FIELD_NAME}: pwd",
    ]
    ),
    ("20 1 3 5 1 pwd", 
     [
        f"{MINUTES_FIELD_NAME}: 20",
        f"{HOURS_FIELD_NAME}: 1",
        f"{DAY_OF_MONTH_FIELD_NAME}: 3",
        f"{MONTHS_FIELD_NAME}: 5",
        f"{DAY_OF_WEEK_FIELD_NAME}: 1",
        f"{COMMAND_FIELD_NAME}: pwd",
    ]
    ),
]

exception_test_data = [
    (
        "1,5 1-3,7 5 cmd",
        SyntaxError,
        "Expression size does not match the size of supported time fields 5"
    ),
    (
        "*/60 1,5 1-3,7 5 * cmd",
        ValueError,
        "Start 0 or interval 60 is out of range of the field values 0 and 59"
    ),
    (
        "*//60 1,5 1-3,7 5 * cmd",
        ValueError,
        "Invalid expression *//60"
    ),
    (
        "*/6 1,5 1-5-7 5 * cmd",
        ValueError,
        "Invalid expression 1-5-7"
    ),
    (
        "20 1 3 5 ? cmd/temp",
        ValueError,
        "Unsupported expression: ?"
    ),
]

def format_output(output):
    output_values = []
    for key, value in output.items():
        output_values.append(f"{key}: {value}")
    return output_values

@pytest.mark.parametrize("test_input , expected_output", test_data)
def test_parse_expression(test_input , expected_output):
    parsed_dict = parse_expression(test_input)
    assert format_output(parsed_dict) == expected_output

@pytest.mark.parametrize("test_input, error_type, error_message", exception_test_data)
def test_size_of_fields(test_input, error_type, error_message):
    with pytest.raises(error_type) as error_info:
        parse_expression(test_input)
    assert str(error_info.value) == error_message
