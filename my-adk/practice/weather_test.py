import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 37.5665,
    "longitude": 126.9780,
    "current_weather": True,
}

response = requests.get(url, params=params)
#print(response.status_code)
#print(response.json())

data = response.json()
current = data["current_weather"]

print("기온 :", current["temperature"])
print("풍속 :", current["windspeed"])
print("날씨코드 :", current["weathercode"])

