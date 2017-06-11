# signup at http://www.cricapi.com/
# get your unique api key and put it in the apikey key
# the api key will be a 19-digit alphanumeric key
# make sure you have requests library installed on your system
# to install it case, it isn't available, type
# pip install requests 
# on your terminal

import json, requests


#only see updates from your favourite teams
fav_teams = list()
fav_teams = ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'West Indies']

# this part will deal with fetching the unique id from the API
# it will send a json request and receive a JSON response

#dictionary to 
myDict = dict()

# API URL
URL = 'http://cricapi.com/api/cricket'

# defining a json request dictionary here which is to be sent to the API
# enter your API key here
json_req = {
	"apikey" : ""
}

# sending GET request
# saving response as response object
req = requests.post(url=URL, params=json_req)

# extracting data in json format
match_info = req.json()

#
search_key = 'data'
inner_search_key = 'unique_id'

#parsing response JSON and storing values in our dictionary
for outer_key, outer_value in match_info.items():
	if search_key == outer_key:
		key_fetch = match_info.get(outer_key)
		for iterator in key_fetch:
			for inner_key, inner_value in iterator.items():
				if inner_search_key == inner_key:
					unique_id = inner_value
					myDict.update({'unique_id' : unique_id})

#for k, v in myDict.items():
#	print(k, v)


# this part will now deal with fetching scores for the ongoing cricket matches
# using the fetched and stored uniqueid earlier