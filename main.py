
from datetime import datetime
import requests
import json
import key

map_id = 40540
api_key = key.key
api_url = f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={api_key}&mapid={map_id}&max=2&outputType=JSON"
response = requests.get(api_url)
data = json.loads(response.content)
train = data['ctatt']['eta'][0]
station = data['ctatt']['eta'][0]['staNm']
dest = data['ctatt']['eta'][0]['destNm']
arrival_time = datetime.strptime(train['arrT'], '%Y-%m-%dT%H:%M:%S')
timetillarival = (arrival_time - datetime.now()).total_seconds()
hours = int(timetillarival // 3600)
minutes = int((timetillarival % 3600) // 60)
seconds = int(timetillarival % 60)
print(f"Next train arriving at {station} towards {dest} is in {hours} hour(s), {minutes} minute(s), {seconds} second(s).")
