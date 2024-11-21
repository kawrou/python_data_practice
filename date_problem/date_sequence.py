import json
from datetime import datetime, timedelta

def load_test_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    data = load_test_data("test_input.json")

    dates_obj_lst = [datetime.strptime(item["date"], "%Y-%m-%dT%H:%M:%S.%fZ") for item in data]
    start_date = min(dates_obj_lst)
    end_date = max(dates_obj_lst)

    print(start_date, end_date)
if __name__ == "__main__":
    main() 
