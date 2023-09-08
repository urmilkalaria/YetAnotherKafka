import json
import subprocess
import time 
import os
with open('settings.json','r+') as f:
	global settings
	settings = json.load(f)


def check_port_open():
	for i in range(8080,9100):
		if str(i) not in settings['broker_port'][0].keys():
			command = f'netstat -ano | find "{i}" | find "LISTEN"'
			process = process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
			l = process.communicate()[0].decode().strip().split()
			if not(len(l)):
				return str(i)

while True:
	time.sleep(2)
	down = []
	for i in settings['broker_port'][0]:

		command = f'netstat -ano | find "{i}" | find "LISTEN"'
		# print(command)
		process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		l = process.communicate()[0].decode().strip().split()
		if len(l):
			command = f'tasklist /fi "PID eq {l[-1]}"'

			process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
			out = process.communicate()[0].decode().strip()
			if "python" in out:
				print("broker port available",i)
			else:
				print("broker port not available",i)
				down.append(i)
		else:
			print("broker port open") 
	print(down)   
	for i in down:

		val = settings['broker_port'][0].pop(i)
		print(val)
		settings['broker_port'][0][check_port_open()] = val

		os.remove('settings.json')
		with open('settings.json', 'w') as f:
			json.dump(settings, f)
	if str(settings['Leader']) not in settings['broker_port'][0].keys():
		print("here")
		settings['Leader'] = int(list(settings['broker_port'][0].keys())[0])

		os.remove('settings.json')
		with open('settings.json', 'w') as f:
			json.dump(settings, f)


