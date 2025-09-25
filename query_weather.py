import requests
from credentials import OWM_API_KEY

API_KEY = OWM_API_KEY
LAT = 60.1699     # Helsinki latitude
LON = 24.9384     # Helsinki longitude

url = f"https://api.openweathermap.org/data/3.0/onecall?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Check for alerts
alerts = data.get("alerts", [])
if alerts:
    for alert in alerts:
        print(f"Source: {alert['sender_name']}")
        print(f"Event: {alert['event']}")
        print(f"Start: {alert['start']}")
        print(f"End: {alert['end']}")
        print(f"Description: {alert['description']}")
        print("-" * 30)
else:
    print("No active government weather alerts for this location.")

