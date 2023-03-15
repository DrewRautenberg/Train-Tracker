from datetime import datetime
import requests
import json
import key


def call(map_id):
    api_key = key.key
    max_results = 4
    api_url = f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key=" \
              f"{api_key}&mapid={map_id}&max={max_results}&outputType=JSON"
    response = requests.get(api_url)
    data = json.loads(response.content)
    i = 0
    while i <= max_results - 1:
        train = data['ctatt']['eta'][i]
        station = data['ctatt']['eta'][i]['staNm']
        dest = data['ctatt']['eta'][i]['destNm']
        is_due = data['ctatt']['eta'][i]['isApp']
        arrival_time = datetime.strptime(train['arrT'], '%Y-%m-%dT%H:%M:%S')
        time_till_arrival = (arrival_time - datetime.now()).total_seconds()
        hours = int(time_till_arrival // 3600)
        minutes = int((time_till_arrival % 3600) // 60)
        seconds = int(time_till_arrival % 60)
        if is_due == "1":
            print(f"Next train arriving at {station} towards {dest} is due.")
        else:
            print(
                f"Next train arriving at {station} towards {dest} is in {hours} hour(s), "
                f"{minutes} minute(s), {seconds} second(s).")
        i += 1
