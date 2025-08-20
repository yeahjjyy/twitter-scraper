import requests


# get token from https://www.twexapi.io/dashboard
token = ""
# get the cookie from the browser
cookie = ""

url = "https://api.twitterxapi.com/twitter/tweets/create"

payload = {
    "cookie": cookie,
    "tweet_content": "hello,twitter"
}
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())