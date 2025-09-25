import json

def format_alert(alert):
    # Format a single alert dict as a readable string
    # Adjust formatting as you like for Slack
    lines = [
        f"*Event:* {alert.get('event', 'Unknown')}",
        f"*Issued by:* {alert.get('sender_name', 'Unknown')}",
        f"*Start:* <t:{alert.get('start', '0')}:f> (Unix: {alert.get('start', '0')})",
        f"*End:* <t:{alert.get('end', '0')}:f> (Unix: {alert.get('end', '0')})",
        f"*Description:*\n{alert.get('description', '')}"
    ]
    return "\n".join(lines)

def format_alerts_for_slack(alerts_json):
    # Accepts a dict with 'alerts' key as from OWM
    alerts = alerts_json.get("alerts", [])
    if not alerts:
        result = "_No active weather alerts._"
    else:
        sections = [f"Alert #{i+1}\n{format_alert(alert)}" for i, alert in enumerate(alerts)]
        result = "\n\n".join(sections)
    return {"text": result}

