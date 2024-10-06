from parser.constants import *
from parser.field import Field, FieldType

class FieldFactory:

    def get_field(self, field_type : FieldType):
        """Constructs the object for the time field according to the type of the field"""
        match field_type:
            case FieldType.MINUTE:
                return Field(MINUTES_START_VALUE, MINUTES_END_VALUE, MINUTES_FIELD_NAME)
            case FieldType.HOUR:
                return Field(HOURS_START_VALUE, HOURS_END_VALUE, HOURS_FIELD_NAME)
            case FieldType.DAY_OF_MONTH:
                return Field(DAY_OF_MONTH_START_VALUE, DAY_OF_MONTH_END_VALUE, DAY_OF_MONTH_FIELD_NAME)
            case FieldType.MONTH:
                return Field(MONTHS_START_VALUE, MONTHS_END_VALUE, MONTHS_FIELD_NAME)
            case FieldType.DAY_OF_WEEK:
                return Field(DAY_OF_WEEK_START_VALUE, DAY_OF_WEEK_END_VALUE, DAY_OF_WEEK_FIELD_NAME)
            case _:
                raise NotImplementedError(f"Unsupported field_type: {str(field_type)}")

factory = FieldFactory()