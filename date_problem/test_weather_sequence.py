import pytest
from weather_sequence import main

def test_main():
    expected_output = [
    {"date": "2023-11-01T06:00:00.000Z", "temperature": 15},
    {"date": "2023-11-02T12:00:00.000Z", "temperature": None},
    {"date": "2023-11-03T07:00:00.000Z", "temperature": 20},
    {"date": "2023-11-03T09:00:00.000Z", "temperature": 22},
    {"date": "2023-11-04T12:00:00.000Z", "temperature": None},
    {"date": "2023-11-05T08:00:00.000Z", "temperature": 18}
    ]

    output = main()
    assert output == expected_output
