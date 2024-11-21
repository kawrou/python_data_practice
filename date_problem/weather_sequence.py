from datetime import datetime, timedelta, date
import json
from typing import TypedDict, List, Dict, Tuple
#input: [{"date": "2023-11-01T06:00:00.000Z", "temperature": 15}, ...]
#Output: print(json.dumps(), indent=4)
#Generate a new dataset that:
#Includes all the dates from earliest to the latest
#Fill any missing entries with "time" set to "T12:00:00.000Z" and "temperature" to None.

sample_data = [
    {"date": "2023-11-03T09:00:00.000Z", "temperature": 22},
    {"date": "2023-11-01T13:00:00.000Z", "temperature": 20},
    {"date": "2023-11-01T09:00:00.000Z", "temperature": 15},
]

#Output: 
#[
#    {"date": "2023-11-01T09:00:00.000Z", "temperature": 15},
#    {"date": "2023-11-01T13:00:00.000Z", "temperature": 20},
#    {"date": "2023-11-02T09:00:00.000Z", "temperature": None},
#    {"date": "2023-11-03T09:00:00.000Z", "temperature": 22},
#]

# sort the sample data
# get the start date and end date
# create a new dictionary with the sample data for easier lookup and extraction
# create a new list

class DataItem(TypedDict):
    date: str
    temperature: float | None

DataList = List[DataItem]
GroupedData = Dict[date, DataList]

date_pattern = "%Y-%m-%dT%H:%M:%S.%fZ"

def load_test_data(file_path: str) -> DataList:
    with open(file_path, "r") as f:
        return json.load(f)

def main() -> DataList:
#    data = sample_data    
    data = load_test_data("weather_data.json")

    sorted_data = sort_data_by_date(data)
    start_date, end_date = get_start_end_date(sorted_data)
    grouped_data = group_data(sorted_data)
    updated_data = fill_missing_data(start_date, end_date, grouped_data)

    print(json.dumps(updated_data, indent=4))
    return updated_data

#function works correctly
def sort_data_by_date(data: DataList) -> DataList:
    return sorted(data, key=lambda item: item["date"])

#functions works correctly
def get_start_end_date(data: DataList) -> Tuple[datetime, datetime]:
    start_date = datetime.strptime(data[0]["date"], date_pattern)
    end_date = datetime.strptime(data[-1]["date"], date_pattern)
    return (start_date, end_date)

#function works correctly
def group_data(data: DataList) -> GroupedData:
    grouped_items = {}
    for item in data:
        date_obj = datetime.strptime(item["date"], date_pattern).date()
        if date_obj not in grouped_items:
            grouped_items[date_obj] = []
        grouped_items[date_obj].append(item)
    return grouped_items

#function works correctly
def fill_missing_data(
    start_date: datetime, 
    end_date: datetime, 
    grouped_data: GroupedData
) -> DataList:
    current_date = start_date

    new_data = []
    while current_date <= end_date:
        if current_date.date() not in grouped_data:
            missing_date = current_date.date()
            new_data.append({"date": f"{missing_date}T12:00:00.000Z", "temperature": None})
        else:
            new_data.extend(grouped_data[current_date.date()])

        current_date += timedelta(days=1)
     
    return new_data

if __name__ == "__main__":
    main() 
