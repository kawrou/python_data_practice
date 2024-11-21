import json
from datetime import datetime, timedelta
from collections import defaultdict

# Output:
# for missing dates -> T05:00:00.000Z
# value -> 0
# print an array of object and be sure to call json.dumps on the final object

# Get the start date and end date
# create a list
# if the dates already exist then use the original date
# if it doesn't, create a new date with a default time
# if the date exist, use the original value
# if the date doesn't exist, set the value to 0

sample_data = [
    {
        "date": "2022-02-08T06:00:00.000Z",
        "value": 40
    },
    {
        "date": "2022-02-10T13:10:00.000Z",
        "value": 10
    },
    {
        "date": "2022-02-10T13:15:00.000Z",
        "value": 20
    },
] 

date_pattern = "%Y-%m-%dT%H:%M:%S.%fZ"

def load_test_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    data = load_test_data("test_input.json")
    #data = sample_data

    sorted_dates = sort_dates(data)
    start_date, end_date= get_start_end_date(sorted_dates)
    #grouped_dates = group_items_by_date(sorted_dates)
    grouped_dates = group_items_by_date(sorted_dates)

    result = fill_missing_dates(start_date, end_date, grouped_dates)
    print(json.dumps(result, indent=4))

def group_items_by_date(data):
    grouped = {}
    for item in data:
        item_date = datetime.strptime(item["date"], date_pattern).date()
        if item_date not in grouped:
            grouped[item_date] = []
        grouped[item_date].append(item)
    return grouped

def group_items_by_date_alternative(data):
    grouped = defaultdict(list)
    for item in data:
        item_date = datetime.strptime(item["date"], date_pattern).date()
        grouped[item_date].append(item)

def get_start_end_date(sorted_dates):
    start_date = sorted_dates[0]["date"]
    end_date = sorted_dates[-1]["date"]
    return [
        datetime.strptime(start_date, date_pattern), 
        datetime.strptime(end_date, date_pattern)
    ]

def sort_dates(data):
    return sorted(data, key=lambda x : x["date"])

def fill_missing_dates(start_date, end_date, grouped_dates):
    result = []
    current_date = start_date

    while current_date <= end_date:
        if current_date.date() in grouped_dates:
            existing_item = grouped_dates[current_date.date()]
            print(existing_item)
            result.extend(existing_item)
        else:
            formatted_date = current_date.strftime("%Y-%m-%dT05:00:00.000Z")
            result.append({"date":formatted_date, "value": 0})
        current_date += timedelta(days=1)

    return result

if __name__ == "__main__":
    main() 
