from datetime import datetime

current_datetime = datetime.now()
formatted_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
parsed_datetime = datetime.strptime("2023-01-15 12:30:00", "%Y-%m-%d %H:%M:%S")

print("Current Datetime:", current_datetime)
print("Formatted String:", formatted_str)
print("Parsed Datetime:", parsed_datetime)
