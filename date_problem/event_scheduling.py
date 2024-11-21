from datetime import datetime, timedelta, date
import json
from typing import TypedDict, List, Dict, Tuple

#Input:
#Given a list of events which is a list of dicts
#start_time: "2023-11-20T09:00:00.000Z"
#end_time: same format as above
#title: str - "Opening keynote"

#Output:
# A summary of the event schedule:
# {
#    total: Int
#    earliest_start: date string 
#    latest_end: date string
#    duration: float
#}

# Sorted schedule
# concatenate events that overlap
# by using the earliest start time and latest end time
# and combining the event titles

# How:

# need to groupt the events by the date

# Creating a summary:
# Calculate total by counting the length of the list
# get earliest start time by filtering or sorting the list by the start time
# get the latest end time by filtering or sorting the list by the end time
# Calculate the duration by subtracting the end time by the start time

# sorting the schedule:
# concat events

date_pattern = "%Y-%m-%dT%H:%M:%S.%fZ"

def load_test_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    data = load_test_data("events_data.json")
  
    grouped_events = group_events_by_date(data)
    
    summary = create_summary(grouped_events)
    print(json.dumps(summary, indent=4))

    merged_events = merge_events(grouped_events)
    print(json.dumps(merged_events, indent=4))

def merge_events(events):
    return {str(date) : detect_overlap(events[date]) for date in events}

def detect_overlap(events: List) -> List[Dict]: 
    merged_events = []

    current_event = events[0].copy() 

    for i in range(1, len(events)):
        next_event = events[i]
        next_start = datetime.strptime(next_event["start_time"], date_pattern)
        current_end = datetime.strptime(current_event["end_time"], date_pattern)
        
        if next_start <= current_end:
            current_event["end_time"] = max(current_event["end_time"], events[i]["end_time"])
            current_event["title"] += f", {events[i]["title"]}"
        else:
            merged_events.append(current_event)
            current_event = next_event.copy()

    merged_events.append(current_event)
    
    return merged_events

# function works
def group_events_by_date(events: List) -> Dict[date, List]:
    grouped_data = {}
    
    for event in events:
        date = datetime.strptime(event["start_time"], date_pattern).date()
        if date not in grouped_data:
            grouped_data[date] = []
        grouped_data[date].append(event)

    for date_key in grouped_data:
        grouped_data[date_key].sort(key=lambda e: e["start_time"])

    return grouped_data

# funciton should be working
def create_summary(events: Dict) -> Dict:
    summary = {}

    for date, events_list in events.items():
        total_events = get_number_of_events(events_list)

        earliest_time = min(events_list, key=lambda e: e["start_time"])["start_time"]
        latest_time = max(events_list, key=lambda e: e["end_time"])["end_time"]
        duration = calculate_duration(earliest_time, latest_time)
        
        summary[str(date)] = {
            "total_events": total_events,
            "earliest_start": earliest_time,
            "latest_end": latest_time,
            "total_duration_hours": float(duration)
        }

    return summary

# function works
def get_number_of_events(data: List) -> int:
    return len(data) 

# function works
def get_earliest_start_time(data: List) -> str:
    sorted_list = sorted(data, key=lambda event: event["start_time"])
    return sorted_list[0]["start_time"]

# function works
def get_latest_end_time(data: List) -> str:
    sorted_list = sorted(data, key=lambda event: event["end_time"])
    return sorted_list[-1]["end_time"]

# function works
def calculate_duration(start_time, end_time):
    start = datetime.strptime(start_time, date_pattern)
    end = datetime.strptime(end_time, date_pattern)
    return (end - start).total_seconds() / 3600 

if __name__ == "__main__":
    main() 
