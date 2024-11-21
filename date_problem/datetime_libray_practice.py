from datetime import datetime, timedelta, timezone
import calendar
# use datetime.strptime to convert date string into a datetime object
# %Y - Four-digit year
# %m - Two-digit month
# %d - Two-digit day
# %H - Two-digit hour (24-hour format)
# %M - Two-digit minute
# %S - Two-digit second
# %f - microseconds 
# %z - time zone offests

# %B - Month as locale's full name
# %I - 12 hour clock with padded 0

# use datetime.strftime to turn datetime object back into a string

# You can use the timedelta class to generate missing dates
# start_date = datetime(2022, 3, 15)
# for i in range(5):
#   print(start_date + timedelta(days=i))

# datetime objects can be compared and sorted directly:
# date1 = datetime(2022, 3, 15)
# date2 = datetime(2022, 3, 20)

# print(date1 < date2)
# print(date1 == date2)

# dates = [date2, date1]
# sorted_dates = sorted(dates)
# print(sorted_dates)

# Question 1: Parsing and Formatting Dates
# 1: Parse the string "2023-11-20 14:30:00" into a datetime object.
# 2: Convert the datetime object back into a string in the format "November 20, 2023, 2:30PM"
# 3: Parse the string "20/11/2023" using the DD/MM/YYYY format

def parse_and_format_dates ():
    date1 = "2023-11-20 14:30:00"

    parsed_date = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")

    formatted_date = parsed_date.strftime(f"%B %d, %Y, %-I:%M %p")

    return formatted_date

# Question 2: Calculate the difference between dates:
# 1: Calculate how many days are left until your next birthday.
# 2: Find out how many days have passed since January 1, 2000.
# 3: Calculate the difference (in days and hours) between 2023-11-20 12:00:00 AND 2023-11-22 15:45:00
def calculate_till_next_birthday ():
    next_birthday = "25/09/2025"
    parsed_next_birthday = datetime.strptime(next_birthday, "%d/%m/%Y")

    current_date = datetime.now()

    days_left_to_bday = (parsed_next_birthday - current_date)
    return(days_left_to_bday.days)

def calculate_days_passed ():
    start_date = "January 1, 2000"
    parsed_start_date = datetime.strptime(start_date, "%B %d, %Y")
    
    current_date = datetime.now()

    days_passed = (current_date - parsed_start_date)
    return(days_passed.days)

def calculate_difference_between_two_dates ():
    start_date = "2023-11-20 12:00:00"
    end_date = "2023-11-22 15:45:00"

    parsed_start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    parsed_end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    difference = (parsed_end_date - parsed_start_date)

    days = difference.days
    seconds = difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"The time between {start_date} and {end_date} is {days} days, {hours} hours, and {minutes} minutes."

# Question 3: Increment and Decrement Dates:
# 1: Add 30 days to today's date.
# 2: Subtract 2 weeks from a given date (2023-12-01)
# 3: Generate a list of all the dates for the next 7 days starting from today.

def add_thirty_days_from_today ():
    now = datetime.now()
    new_date = now + timedelta(days=30)
    formatted_new_date = new_date.strftime("%d/%m/%Y")
    return(formatted_new_date)

def subtract_two_weeks_from_given_date (date):
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expect format: YYYY-MM-DD")

    new_date = parsed_date - timedelta(weeks=2)

    return new_date.strftime("%Y-%m-%d")

def dates_for_next_seven_days (num_days=7):
    now = datetime.now()

    return [(now + timedelta(days=x)).strftime("%d/%m/%Y") for x in range(num_days)]

# Question 4: Working with Ranges of Dates
# 1: Return a list of dates between a start date and an end date
# 2: Modify the above function to skip weekends
# 3: Write a funciton that calculates the number of Mondays between two dates.
def list_of_dates_between_dates (start_date=None, end_date=None):
    if not start_date:
        start_date = datetime.now()
    if not end_date:
        end_date = start_date + timedelta(weeks=1)

    days_between = (end_date - start_date).days

    date_list = [start_date + timedelta(days=x) for x in range(1,days_between)]
    
    return [date.strftime("%Y-%m-%d") for date in date_list]

def list_dates_without_weekend ():
    date_list = list_of_dates_between_dates()

    weekdays_only = [date for date in date_list if datetime.strptime(date, "%Y-%m-%d").weekday() < 5]

    return weekdays_only

def count_mondays (date1, date2):
    try:
        parsed_d1 = datetime.strptime(date1, "%Y-%m-%d") 
        parsed_d2 = datetime.strptime(date2, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Expect format: YYYY-MM-DD")

    #start_date = parsed_d1 if parsed_d1 < parsed_d2 else parsed_d2
    #end_date = parsed_d1 if parsed_d1 > parsed_d2 else parsed_d2
    
    start_date = min(parsed_d1, parsed_d2)
    end_date = max(parsed_d1, parsed_d2)

    #K = (end_date - start_date).days

    #date_list = [start_date + timedelta(days=x) for x in range(K+1) if (start_date + timedelta(days=x)).weekday() == 0]
    
    while start_date.weekday() != 0:
        start_date += timedelta(days=1)

    mondays_count = 0
    while start_date <= end_date:
        mondays_count +=1
        start_date += timedelta(days=7)

    return f"There are {mondays_count} Mondays between {start_date.strftime("%Y-%m-%d")} and {end_date.strftime("%Y-%m-%d")}"

# Question 5: Comparing and Sorting Dates
# 1: Compare two datetime objects to determine which is earlier.
# 2: Sort a list of date strings: dates = ["2023-11-25", "2023-11-20", "2023-11-22"]

def determine_earlier_date (date1, date2):
    # e.g. 2022-03-24
    parsed_d1 = datetime.strptime(date1, "%Y-%m-%d") 
    parsed_d2 = datetime.strptime(date2, "%Y-%m-%d")

    return parsed_d1.strftime("%Y-%m-%d") if parsed_d1 < parsed_d2 else parsed_d2.strftime("%Y-%m-%d")

def sort_date_string (dates=None, descending=False):
    if not dates:
        dates = ["2023-11-25", "2023-11-20", "2023-11-22"]

    if descending:
        print("Sorted in descending order:")
    else:
        print("Sorted in ascending order:")

    return sorted(dates, reverse=descending)


# Question 6: Creating Timestamps
# 1: Get the current date and time and format it as "YYYY-MM-DD HH:MM:SS"
# 2: Add that timestamp to a log message e.g. [time stampe] User logged in.

def current_date ():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def add_current_date_to_log_message (message="User logged in"):
    date_string = current_date()
    return f"[{date_string}]: {message}."

# Question 7: Practice Timezone Handling
# 1: Get the current time in UTC.
# 2: Convert a local datetime object to UTC
# 3: Parse a date string with a timezone offest (e.g. "2023-11-20T14:30:00+02:00")

def current_time_utc ():
    return datetime.now(timezone.utc)

def convert_local_to_utc(local_datetime):
    if local_datetime.tzinfo is None:
        raise ValueError("The datetime object must have timezone information")

    return local_datetime.astimezone(timezone.utc)

# %z - allows parsing strings with timezone offsets like +02:00 or -05:00
def parse_and_convert_to_utc(date_string):
    dt_with_offset = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S%z")
    dt_utc = dt_with_offset.astimezone(timezone.utc)
    return dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC")

# Challenge:
# 2: Write a function that takes a start date and a number of working days and returns the date after skipping weekends (because working days)
# 3: Generate ISO 8601 Timestamps: Write a function that takes a lit of datetime objects and converst them into ISO 8601 strings (e.g. "2023-11-20T14:30:00Z")

