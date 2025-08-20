import requests
# get token from https://www.twexapi.io/dashboard
token = ""
# online get search terms https://advance-search.twitterxapi.com/
search_terms = ["from:elonmusk"]
# sort by latest, popular, or top
sort_by = "Latest"
# max items to return
max_items = 10
# get the data from the api
data = {
    "maxItems": max_items,
    "sortBy": sort_by,
    "searchTerms": search_terms
}

url = "https://api.twitterxapi.com/twitter/advanced_search"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers)

print(response.json())