import requests

API_KEY = API_KEY
SEARCH_QUERY = "space exploration"

url = "https://www.googleapis.com/youtube/v3/search"
params = {
    "part": "snippet",
    "q": SEARCH_QUERY,
    "type": "video",
    "maxResults": 5,
    "key": API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for item in data.get("items", []):
        title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        print(f"Title: {title}\nURL: https://www.youtube.com/watch?v={video_id}\n")
else:
    print(f"Error: {response.status_code}", response.text)
