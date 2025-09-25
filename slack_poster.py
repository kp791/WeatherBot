import requests
import json
import test_data_generator as tdg
import weather_parser as wp
import query_weather
from credentials import SLACK_WEBHOOK_URL

# Replace with your Slack webhook trigger URL (from Workflow Builder)
webhook_url = SLACK_WEBHOOK_URL

# Test data
# data = wp.format_alerts_for_slack(tdg.generate_alerts(1))

# Real data
data = wp.format_alerts_for_slack(query_weather.data)

# POST request to the Slack workflow webhook
response = requests.post(webhook_url, json=data)

# Print Slack’s response/status for debugging
print('Status code:', response.status_code)
print('Response:', response.text)

