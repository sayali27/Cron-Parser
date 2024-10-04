from parser.constants import *
from parser.field import Field, FieldType


class FieldFactory:
    def get_field(self, field_type : FieldType):
        match field_type:
            case FieldType.MINUTE:
                return Field(MINUTES_START_VALUE, MINUTES_END_VALUE, "minute")
            case FieldType.HOUR:
                return Field(HOURS_START_VALUE, HOURS_END_VALUE, "hour")
            case FieldType.DAY_OF_MONTH:
                return Field(DAY_OF_MONTH_START_VALUE, DAY_OF_MONTH_END_VALUE, "day of month")
            case FieldType.MONTH:
                return Field(MONTHS_START_VALUE, MONTHS_END_VALUE, "month")
            case FieldType.DAY_OF_WEEK:
                return Field(DAY_OF_WEEK_START_VALUE, DAY_OF_WEEK_END_VALUE, "day of week")
            case _:
                print(f"{field_type} Came in default case") 
                return Field(0, 0)

factory = FieldFactory()