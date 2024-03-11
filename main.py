import os
from dotenv import load_dotenv
import requests


load_dotenv()
api_key = os.getenv("API_KEY")
base_url = "https://api.amctheatres.com"
now_playing_url = base_url + "/v2/movies/views/now-playing"
headers = {
    "X-AMC-Vendor-Key": api_key
}

if __name__ == "__main__":
    res = requests.request("GET", now_playing_url, headers=headers)
    print(res.status_code)
    print(res.json())
    