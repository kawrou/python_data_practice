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
  
    # This groups the events by the date, and it is already sorted by earliest start time
    grouped_events = group_events_by_date(data)
    
    summary = create_summary(grouped_events)
    print(summary)

    merged_events = merge_events(grouped_events)
    print(merged_events)

def merge_events(events):
   # merged_events = {}
   # for date in events:
   #     merged_events[str(date)] = detect_overlap(events[date])

    #return merged_events
    return {str(date) : detect_overlap(events[date]) for date in events}

def detect_overlap(events: List): 
    events_list = []

    event_data = {
        "start_time": "", 
        "end_time": "", 
        "title": ""
    }

    current_end = datetime.strptime(events[0]["end_time"], date_pattern)

    for i in range(len(events)):
        next_start = datetime.strptime(events[i]["start_time"], date_pattern)
        if i  == 0:
            event_data = {  # Create a new dictionary
                "start_time": events[i]["start_time"], 
                "end_time": events[i]["end_time"], 
                "title": f"{events[i]['title']}, "
            }

        elif i == (len(events)-1):
            event_data["end_time"] = events[i]["end_time"] 
            event_data["title"] += f"{events[i]["title"]}"
            events_list.append(event_data)

        elif next_start < current_end:
            event_data["end_time"] = events[i]["end_time"] 
            event_data["title"] += f"{events[i]["title"]}, "

        else:
            event_data["title"] = event_data["title"].strip(", ")
            events_list.append(event_data)

            current_end = datetime.strptime(events[i]["end_time"], date_pattern)
            event_data = {  # Create a new dictionary for the next event
                "start_time": events[i]["start_time"],
                "end_time": events[i]["end_time"],
                "title": f"{events[i]['title']}, "
            }

    return events_list

# function works
def group_events_by_date(events: List) -> Dict[date, List]:
    grouped_data = {}
    
    for event in events:
        date = datetime.strptime(event["start_time"], date_pattern).date()
        if date not in grouped_data:
            grouped_data[date] = []
        grouped_data[date].append(event)

    return grouped_data

# funciton should be working
def create_summary(events: Dict) -> Dict:
    summary = {}

    for date in events:
        events_list = events[date]
        total_events = get_number_of_events(events_list)
        earliest_time = get_earliest_start_time(events_list)
        latest_time = get_latest_end_time(events_list)
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
    return (end - start).seconds // 3600 

if __name__ == "__main__":
    main() 
