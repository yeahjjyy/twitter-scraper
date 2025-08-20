import requests
# get token from https://www.twexapi.io/dashboard
token = ""
# get the following of a user
username = "elonmusk"
# get the number of following
max_following = 10000

url = f"https://api.twitterxapi.com/twitter/following/{username}/{max_following}"

headers = {"Authorization": f"Bearer {token}"}

response = requests.get(url, headers=headers)

print(response.json())