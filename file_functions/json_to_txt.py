# Commit made by Dhruv Sharma, SRN: PES1UG20CS129. Original by Kshitij Sharma, SRN: PES1UG20CS223
import json
import datetime
def json_to_txt(txt_name, json_name):
	with open(json_name, 'r+') as f:
		settings = json.load(f)
	with open(txt_name, 'a+') as f:
		f.write("["+str(datetime.datetime.now())+']'+'\t'+str(settings))
		f.write('\n')

