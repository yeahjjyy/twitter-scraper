import requests
# get token from https://www.twexapi.io/dashboard
token = ""
# get the followers of a user
username = "elonmusk"
# get the number of followers
max_followers = 10000

url = f"https://api.twitterxapi.com/twitter/followers/{username}/{max_followers}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())