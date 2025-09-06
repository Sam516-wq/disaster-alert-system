import requests

url = "http://127.0.0.1:5000/create_alert"

data = {
    "disaster_time": "2025-09-02T18:00:00",
    "zone": "Zone A",
    "message": "⚠️ Test Alert: Flood expected in Zone A."
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())
