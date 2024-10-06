def output_values(parsed_values):
    """Prints the schedule for each time field in table format"""
    for key, value in parsed_values.items():
        print(f"{key}".ljust(14)+f"{value}")