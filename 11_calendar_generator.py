import calendar

# Function to print the calendar for a given month and year
def print_calendar(year, month):
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    # Get the first day of the month and number of days in the month
    start_day, num_days = calendar.monthrange(year, month)

    # Print spaces for the days before the start of the month
    for _ in range(start_day):
        print("  ", end=" ")

    # Print the days of the month
    for day in range(1, num_days + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day) % 7 == 0:
            print()

# Example usage
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
print_calendar(year, month)
