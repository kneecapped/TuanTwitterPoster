from datetime import date
from twilio.rest import TwilioRestClient
import twitter_request
import json
import time

# To find these visit https://www.twilio.com/user/account

TUAN_ID= '#T'
def main():
	Key_file_path="/root/venv0/key.json"
	Log_file_path="/root/venv0/twitterbot/posts.log"

	with open(Key_file_path) as json_data:
		data = json.load(json_data)
	json_data.close()
	ACCOUNT_SID = data["ACCOUNT_SID"]
	AUTH_TOKEN = data["AUTH_TOKEN"]
	PHONE_NUMBER = data["PHONE_NUMBER"]
	TUAN_ID= '#T'
	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	while True:
		time.sleep(10)
		messages = client.messages.list()
		Message_to_post_twitter = []

		for message in messages:
		    if message.body[:2].upper() == TUAN_ID:
		    	Message_to_post_twitter.append(message.body[2:].lstrip())
		    try:
		    	message.delete()
		    except:
		    	pass

		log_file = open(Log_file_path,'a')
		for each in Message_to_post_twitter:
			try:
				twitter_request.POST_TO_TWITTER(each[:140].upper())
				print "{0} posted.".format(each)
				log_file.write("{0} posted.\n".format(each))
			except:
				print each,"passed."
				log_file.write("{0} posted.\n".format(each))
				pass

if __name__ == "__main__":
	main()