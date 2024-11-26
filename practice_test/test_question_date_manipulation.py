from datetime import datetime, timedelta, date
import json
from typing import Dict
# Sort the data by date in ascending order.
# Fill in any missing dates between the earliest and latest date.
# For missing dates:
# Add a new dictionary with a "value": 0
# Use the same time "T08:00:00.000Z" for the missing dates
# Return the updated dataset


# sort the dates
# group the dates?
# Generate a list of dicts from the first date to the last date
# Create a new list using either a dict from the new list or the original list if the data exists
# Return the new list

data = [
    {"date": "2023-11-17T08:00:00.000Z", "value": 20},
    {"date": "2023-11-17T03:00:00.000Z", "value": 20},
    {"date": "2023-11-20T10:00:00.000Z", "value": 25},
    {"date": "2023-11-18T09:00:00.000Z", "value": 15},
    {"date": "2023-11-23T09:00:00.000Z", "value": 15}
]

time_value = "T08:00:00.000Z"
date_pattern = "%Y-%m-%dT%H:%M:%S.%fZ"

def main(data):
    sorted_list = sort_list(data)
    grouped_dates = group_dates(sorted_list)
    min_date, max_date = find_start_end_dates(grouped_dates)
    all_dates = generate_all_dates(min_date, max_date)
    
    updated_data = update_data(all_dates, grouped_dates)
    print(json.dumps(updated_data, indent=4))

    return updated_data

def sort_list(data: list):
    return sorted(data, key=lambda obj: obj["date"])

def group_dates(sorted_list: list):
    dates_map = {}

    for date_data in sorted_list:
        date = datetime.strptime(date_data["date"], date_pattern).date()
        if date not in dates_map:
            dates_map[date] = []
        dates_map[date].append(date_data)

    return dates_map

def find_start_end_dates(grouped_dates: Dict):
    min_date = min(grouped_dates)
    max_date = max(grouped_dates)

    return min_date, max_date

def generate_all_dates(min_date: date, max_date: date) -> list:
    return [min_date + timedelta(days=i) for i in range((max_date - min_date).days + 1)]

def update_data(missing_dates: list, grouped_dates: dict):
    updated_data = []

    for date in missing_dates:
        if date not in grouped_dates:
            new_data = {"date": date.strftime(f"%Y-%m-%d{time_value}"), "value": 0}
            updated_data.append(new_data)
        else:
            updated_data.extend(grouped_dates[date])

    return updated_data

if __name__ == "__main__":
    main(data)
