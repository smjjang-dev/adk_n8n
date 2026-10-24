import requests

CITY_COORDS = {
    "서울": (37.5665, 126.9780),
    "부산": (35.1796, 129.0756),
    "대구": (35.8714, 128.6014),
    "광주": (35.1595, 126.8526),
    "대전": (36.3504, 127.3845),
    "제주": (33.4996, 126.5312),
}


def describe_weather_code(code: int) -> str:
    if code == 0:
        return "맑음"
    if code <= 3:
        return "구름 조금"
    if code in (45, 48):
        return "안개"
    if 51 <= code <= 67:
        return "비"
    if 71 <= code <= 77:
        return "눈"
    if 80 <= code <= 82:
        return "소나기"
    if code >= 95:
        return "뇌우"
    return "알 수 없음"


def get_current_weather(city: str) -> dict:
    """
    지정한 도시의 현재 날씨(기온, 풍속, 날씨 상태)를 조회합니다.

    Args:
        city: 도시 이름. 지원 도시: 서울, 부산, 대구, 광주, 대전, 제주

    Returns:
        city, temperature(℃), windspeed(km/h), condition을 담은 dict.
        지원하지 않는 도시이거나 조회에 실패하면 error 키에 설명을 담아 반환합니다.
    """

    if city not in CITY_COORDS:
        return {"error": f"지원하지 않는 도시입니다: {city}"}

    lat, lon = CITY_COORDS[city]

    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=10,
        )
        response.raise_for_status()

        current = response.json()["current_weather"]

        return {
            "city": city,
            "temperature": current["temperature"],
            "windspeed": current["windspeed"],
            "condition": describe_weather_code(current["weathercode"]),
        }

    except requests.RequestException:
        return {"error": "날씨 정보를 가져올 수 없습니다. 잠시 후 다시 시도하세요."}