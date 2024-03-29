"""Module that querrys api and prints results"""
from datetime import datetime
import json
import requests
import key


def stationSelection(stations):
    """Print station list and get user input"""
    # Print list of stations and their corresponding numbers
    print("Please select a Station:")
    for i, station in enumerate(stations, 1):
        print(f"{i}. {station}")

    # Prompt user for station choice
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1, len(stations) + 1):
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid choice")

    # Call api with the chosen station code
    station_name = list(stations.keys())[choice-1]
    station_code = stations[station_name]
    call(station_code)


def call(map_id):
    """Call api and print results"""
    api_key = key.key
    max_results = 6
    api_url = f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=" \
              f"{api_key}&mapid={map_id}&max={max_results}&outputType=JSON"
    response = requests.get(api_url, timeout=30)
    data = json.loads(response.content)

    for train in data['ctatt']['eta']:
        station = train['staNm']
        dest = train['destNm']
        is_due = train['isApp']
        run = train['rn']
        is_delayed = train['isDly']
        arrival_time = datetime.strptime(train['arrT'], '%Y-%m-%dT%H:%M:%S')
        time_till_arrival = (arrival_time - datetime.now()).total_seconds()
        hours = int(time_till_arrival // 3600)
        minutes = int((time_till_arrival % 3600) // 60)
        seconds = int(time_till_arrival % 60)
        if is_due == "1":
            print(f"Next train arriving at {station} towards {dest} is due.")
        elif is_delayed == "1":
            print(f"Next train arriving at {station} towards {dest} is delayed.")
        else:
            print(
                f"Next train arriving at {station} towards {dest} is run number {run} in "
                f"{hours} hour(s), {minutes} minute(s), {seconds} second(s).")
