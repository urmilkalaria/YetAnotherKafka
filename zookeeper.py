import json
import subprocess
import time 
import os
with open('settings.json','r+') as f:
	settings = json.load(f)


def check_port_open():

	for i in range(8080,9100):
		if str(i) not in settings['broker_port'][0].keys():
			command = f'netstat -lntup |grep {i}'
			process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
			l = process.communicate()[0].decode().strip().split()
			if not(len(l)):
				return str(i)

while True:
	time.sleep(2)
	down = []
	for i in settings['broker_port'][0]:
		print(i)
		command = f'netstat -lntup |grep {i}'
		process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
		l = process.communicate()[0].decode().strip().split()

		if not(len(l)):
			print(i,"is open")
		elif "python3" in l[-1]:	
			print(i,"is down")
			down.append(i)   
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


