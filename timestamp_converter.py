#timestamp: int = int(input("Digite o timestamp: "))
MINUTE_IN_SECONDS = 60
HOUR_IN_SECONDS = MINUTE_IN_SECONDS * 60
DAY_IN_SECONDS = HOUR_IN_SECONDS * 24
WEEK_IN_SECONDS = DAY_IN_SECONDS * 7

timestamp: int = 87426

# hours = timestamp // 3600
# hour_remaining = timestamp % 3600 

# minutes = hour_remaining // 60
# minutes_remaining = hour_remaining % 60
# seconds = minutes_remaining


def convert_and_get_remaining(value: float, divided_by: float) -> (float, float):
    converted_value = value // divided_by
    remaining_value = value % divided_by

    return (converted_value, remaining_value)

weeks, week_remaining = convert_and_get_remaining(timestamp, WEEK_IN_SECONDS)
days, day_remaining = convert_and_get_remaining(week_remaining, DAY_IN_SECONDS)
hours, hour_remaining = convert_and_get_remaining(day_remaining, HOUR_IN_SECONDS)
minutes, minute_remaining = convert_and_get_remaining(hour_remaining, MINUTE_IN_SECONDS)
seconds = minute_remaining

print(f"{weeks} weeks {days:02} day {hours:02}:{minutes}:{seconds:02}")

### VAI CAIR SÉCULOS NO CP