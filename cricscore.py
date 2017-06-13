# signup at http://www.cricapi.com/
# get your unique api key and put wherever mentioned
# the api key will be a 19-digit alphanumeric key
# make sure you have requests library installed on your system
# to install it case, it isn't available, type
# pip install requests 
# on your terminal

import json, requests
import subprocess



# get only updates for your favourite team
def compare(team, alist, id):
	for iterator in alist:
		if team == iterator:
			return id

# desktop pop-up message function
def sendmessage(score_list):
	if not score_list:
		message = "No live matches from your favourite teams!"
		subprocess.Popen(['notify-send', message])
		return

	else:
		for val in score_list:
			subprocess.Popen(['notify-send',val])
			return


# only get updates from your favourite teams
fav_teams = list()
fav_teams = ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka']


# this part will deal with fetching the unique id from the API
# it will send a json request and receive a JSON response

#dictionary to store unique ids for each match
uid_list = list()

# API URL for ongoing matches
URL_match = 'http://cricapi.com/api/matches/'

# defining a json request dictionary here which is to be sent to the API
# enter your API key here
json_req1 = {
	"apikey" : ""
}

# sending GET request
req1 = requests.post(url=URL_match, params=json_req1)

# extracting RESPONSE data in json format
# match_info will return all unique_ids for ongoing matches
match_info = req1.json()

# extracting unique id only
search_key = 'matches'
inner_search_key1 = 'unique_id'
inner_search_key2 = 'team-2'
inner_search_key3 = 'team-1'
matchStarted = 'True'

# parsing response JSON and storing values in our dictionary
for outer_key, outer_value in match_info.items():
	if search_key == outer_key:
		key_fetch = match_info.get(outer_key)
		for iterator in key_fetch:
			for inner_key, inner_value in sorted(iterator.items()):
				if (inner_search_key2 == inner_key) or (inner_search_key3 == inner_key):
					team_name = inner_value
				if (inner_search_key1 == inner_key):
					unique_id = compare(team_name, fav_teams, inner_value)
					uid_list.append(unique_id)
				
# eliminating duplicates 
uid_list = list(set(uid_list))



# this part will now deal with fetching scores for the ongoing cricket matches
# using the fetched and stored uniqueid earlier

#dictionary to store score for each match
score_list = list()

# API URL for selected match scores
URL_score = 'http://cricapi.com/api/cricketScore/'

# processing dictionary for scores of selected teams
for UID in uid_list:
	if UID is not None:
		# defining a json request dictionary here which is to be sent to the API
		# enter your API key here
		json_req2 = {
			"unique_id" : UID,
			"apikey" : ""
		}

		# sending GET request
		req2 = requests.post(url=URL_score, params=json_req2)

		# extracting RESPONSE data in json format
		# match_detail will return all match detail corresponding 
		# to unique id for ongoing matches
		match_detail = req2.json()

		# extracting score values only
		search_key = 'score'

		# parsing response JSON and storing values in score_list dictionary
		for key, value in match_detail.items():
			if search_key == key:
				score_list.append(value)


# eliminating duplicates
score_list =list(set(score_list))

#desktop popup for information on matches
sendmessage(score_list)