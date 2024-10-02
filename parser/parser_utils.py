from unicodedata import numeric
from parser.constants import MINUTES_END_VALUE, MINUTES_START_VALUE


def parse_minutes(mins_regex: str):
    if mins_regex == "*":
        return generate_range(MINUTES_START_VALUE, MINUTES_END_VALUE)
    elif mins_regex.isnumeric():
        return [int(mins_regex)]
    start = -99
    for i in range(len(mins_regex)):
        # if i == 0 and mins_regex[0] == "*":
        #     start = 0
        if mins_regex[i].isnumeric():
            while i < len(mins_regex) and mins_regex[i].isnumeric():
                curr_num = curr_num * 10 + int(mins_regex[i])
            if start != -99:
                end = curr_num
            else:
                start = curr_num
        elif mins_regex[i] == "/":
            interval = 0
            while i < len(mins_regex):
                interval = interval * 10 + int(mins_regex[i])

    
    

def parse_hours(hours_regex: str):
    pass

def parse_day_of_month(days_regex: str):
    pass

def generate_range(start: int, end: int, interval = 1) -> list[int]:
    values = list()
    for value in range(start, end+1, interval):
        values.append(value)
    return values

