import requests
import json
from bs4 import BeautifulSoup

# itunes API documentation
# https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/

## Goal here: code that makes a series of requests to the itunes search API, one for each artist in a list of artists. Just as throwaways -- no caching.
## Should accumulate a list of Python objects (lists or dictionaries!), and for each one, print out the first song name that appears.

baseurl = https://itunes.apple.com/search

artists = ["Kendrick Lamar","Saint Motel","Carly Rae Jepsen"]

# Below, you want to accumulate a list of Python objects that represent the data you get from a request to the itunes API about each artist.

for band in artists:
	artist_responses = [] # HINT: semantic error here...
	params = {"media":"song", "term":band} # HINT: There is a problem in this line; to figure out the problem in this line, you may wanna check out the documentation!
	r = requests.get(baseurl,params)
	result_diction = json.loads(r)
	artist_responses.append(result_diction)

# print(len(artist_responses)) # could be helpful for debugging!
# print(result_diction)

for resp in artist_responses:
	print(resp["results"]["trackName"], "by", resp["results"]["artistName"]) # HINT: error here... try doing more investigation into what resp is, what these nested objects look like: remember, Understand/Extract/Repeat, paste direct json results into jsoneditoronline.org ...
