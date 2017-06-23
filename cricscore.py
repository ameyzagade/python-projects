# signup at http://www.cricapi.com/
# get your unique api key and put wherever mentioned
# the api key will be a 19-digit alphanumeric key
# make sure you have requests library installed on your system
# to install it case, it isn't available, type
# pip install requests 
# on your terminal
#TckzrY1cpOgGCxYUXGwj45HTdTz2
import json, requests
import subprocess



# get only updates for your favourite team
def compare(inner_value, unique_id):
	for iterator in fav_teams:
		if inner_value == iterator:
			print(inner_value, iterator, unique_id)
			return unique_id
		else:
			return

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
	"apikey" : "TckzrY1cpOgGCxYUXGwj45HTdTz2"
}

# sending GET request
req1 = requests.post(url=URL_match, params=json_req1)

# extracting RESPONSE data in json format
# match_info will return all unique_ids for ongoing matches
match_info = req1.json()

# extracting unique id only
search_key = 'matches'
inner_search_key1 = 'unique_id'
inner_search_key2 = 'team-1'
inner_search_key3 = 'team-2'

# parsing response JSON and storing values in our dictionary
for outer_key, outer_value in match_info.items():
	if search_key == outer_key:
		key_fetch = match_info.get(outer_key)
		for iterator in key_fetch:
			for inner_key, inner_value in sorted(iterator.items(), reverse=True):
				if (inner_key == inner_search_key1):
					unique_id = inner_value
				if (inner_key == inner_search_key2) or (inner_key == inner_search_key3):
					abcd = compare(inner_value, unique_id)
					print('abcd', abcd, inner_value)
					uid_list.append(abcd)

				
## eliminating duplicates 
uid_list = list(set(uid_list))
print(uid_list)

#for i in fav_teams:
#	print(i)

# this part will now deal with fetching scores for the ongoing cricket matches
# using the fetched and stored uniqueid earlier

#dictionary to store score for each match
#score_list = list()

# API URL for selected match scores
#URL_score = 'http://cricapi.com/api/cricketScore/'

# processing dictionary for scores of selected teams
#for UID in uid_list:
#	if UID is not None:
		# defining a json request dictionary here which is to be sent to the API
		# enter your API key here
#		json_req2 = {
#			"unique_id" : UID,
#			"apikey" : "TckzrY1cpOgGCxYUXGwj45HTdTz2"
#		}

		# sending GET request
#		req2 = requests.post(url=URL_score, params=json_req2)

		# extracting RESPONSE data in json format
		# match_detail will return all match detail corresponding 
		# to unique id for ongoing matches
#		match_detail = req2.json()

		# extracting score values only
#		search_key = 'score'
#
		# parsing response JSON and storing values in score_list dictionary
#		for key, value in match_detail.items():
#			if search_key == key:
#				score_list.append(value)


# eliminating duplicates
#score_list =list(set(score_list))
#print(score_list)

#desktop popup for information on matches
#sendmessage(score_list)