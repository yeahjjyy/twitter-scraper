import requests

# get token from https://www.twexapi.io/dashboard
token = ""
# get the replies of a tweet
tweet_id = "1957628087228616915"
# get the number of replies
max_replies = 10

url = f"https://api.twitterxapi.com/twitter/tweets/{tweet_id}/replies/{max_replies}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())