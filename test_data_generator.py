import random
import time
import json

SAMPLE_SENDERS = [
    "Finnish Meteorological Institute",
    "NWS Tulsa (Eastern Oklahoma)",
    "Met Office UK",
    "NOAA",
    "Deutscher Wetterdienst"
]
SAMPLE_EVENTS = [
    "Heat Advisory",
    "Flood Watch",
    "Wind Warning",
    "Thunderstorm",
    "Snowfall Warning"
]
SAMPLE_DESCRIPTIONS = [
    "Exercise caution due to high temperatures and humidity.",
    "Flooding possible in low-lying areas.",
    "Strong winds expected in coastal areas.",
    "Severe thunderstorms possible this afternoon.",
    "Heavy snowfall could reduce visibility."
]

def gen_alert(idx):
    now = int(time.time()) + 3600 * idx
    return {
        "sender_name": random.choice(SAMPLE_SENDERS),
        "event": random.choice(SAMPLE_EVENTS),
        "start": now,
        "end": now + 5 * 3600,
        "description": random.choice(SAMPLE_DESCRIPTIONS)
    }

def generate_alerts(n):
    return {"alerts": [gen_alert(i) for i in range(n)]}

sample = generate_alerts(1)
print(json.dumps(sample, indent=2))

