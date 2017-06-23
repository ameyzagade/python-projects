# signup at http://www.cricapi.com/
# get your unique api key and put wherever mentioned
# the api key will be an 19-digit alphanumeric key

import json, requests
import gi
gi.require_version('Notify', '0.7')
from gi.repository import GObject
from gi.repository import Notify


class notif_class(GObject.Object):
	def __init__(self):
		super(notif_class, self).__init__()
		Notify.init("cricscore")

	def send_notification(self, title, text):
		obj = Notify.Notification.new(title, text)
		obj.show()

def compare(inner_value, unique_id):
	# only get updates from your favourite teams
	fav_teams = ['India', 'South Africa']

	for iterator in fav_teams:
		if (inner_value == iterator):
			return unique_id
		else:
			return

# desktop pop-up message function
def sendmessage(score_list):
	score = notif_class()
	
	if not score_list:
		score.send_notification("Bummer!", "No live matches from your favourite team(s) currently!")
		return
	else:
		title = "Live Score"
		for val in score_list:
			score.send_notification(title, val)
		return


def main():
	# this part will deal with fetching the unique id from the API
	# it will send a JSON request and receive a JSON response

	# dictionary to store unique ids for each match
	uid_list = list()

	# API URL for ongoing matches
	URL_match = 'http://cricapi.com/api/matches/'

	# enter your API key here
	json_req1 = {
		"apikey" : ""
	}

	req1 = requests.post(url=URL_match, params=json_req1)

	# match_info will return all unique_ids for ongoing matches
	match_info = req1.json()

	# extracting unique ids only
	search_key = 'matches'
	inner_search_key1 = 'unique_id'
	inner_search_key2 = 'team-2'
	inner_search_key3 = 'team-1'


	# parsing response JSON and storing unique ids in our list
	for outer_key, outer_value in match_info.items():
		if (outer_key == search_key):
			key_fetch = match_info.get(outer_key)
			for iterator in key_fetch:
				for inner_key, inner_value in sorted(iterator.items(), reverse=True):
					if (inner_key == inner_search_key1):
						unique_id = inner_value
					elif (inner_key == inner_search_key2) or (inner_key == inner_search_key3):
						add = compare(inner_value, unique_id)
						uid_list.append(add)
					else:
						pass

				
	# eliminating duplicates form uid list
	uid_list = list(set(uid_list))


	# this part will now deal with fetching scores for the ongoing cricket matches
	# using the fetched and stored unique id earlier

	# dictionary to store score for match of each team
	score_list = list()

	# API URL for selected match scores
	URL_score = 'http://cricapi.com/api/cricketScore/'

	# processing dictionary for scores of selected teams
	for UID in uid_list:
		if UID is not None:
			# enter your API key here
			json_req2 = {
				"unique_id" : UID,
				"apikey" : ""
			}

			req2 = requests.post(url=URL_score, params=json_req2)

			# match_detail will return all match detail corresponding to unique id for ongoing matches
			match_detail = req2.json()

			# extracting score values only
			search_key = 'score'

			# parsing response JSON and storing values in score_list dictionary
			for key, value in match_detail.items():
				if (key == search_key):
					score_list.append(value)

	# eliminating duplicates
	score_list = list(set(score_list))

	#desktop popup for information on matches
	sendmessage(score_list)


if __name__ == "__main__":
	main()