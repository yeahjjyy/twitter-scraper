import requests

# get token from https://www.twexapi.io/dashboard
token = ""
# get the cookie from the browser
cookie = ""
# get the tweet id
tweet_id = "1957628087228616915"

url = "https://api.twitterxapi.com/twitter/tweets/create"

payload = {
    "cookie": cookie,
    "tweet_content": "hello,twitter",
    "reply_tweet_id": tweet_id
}
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())