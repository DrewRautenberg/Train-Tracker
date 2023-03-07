import requests
import json
import key

map_id = 40260
api_key = key.key
api_url = f"https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={api_key}&mapid={map_id}&max=2&outputType=JSON"
response = requests.get(api_url)
data = json.loads(response.content)
train = data['ctatt']['eta'][0]
arrival_time = train['arrT']
print(f"Next train arriving at {arrival_time}")
