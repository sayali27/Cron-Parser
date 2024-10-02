from parser.constants import *
from parser.field import Field, FieldType


class FieldFactory:
    def get_field(self, field_type : FieldType):
        match field_type:
            case FieldType.MINUTE:
                print("minute found!")
                return Field(MINUTES_START_VALUE, MINUTES_END_VALUE)
            case _:
                print(f"{field_type} type found!")
                return Field(0, 0)

factory = FieldFactory()