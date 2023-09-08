def reset():
	
	writer = '{"broker_port": [{"8080": {}, "8081": {}, "8082": {}}], "publisher_port": [5050, 5051, 5052], "consumer_port": [{"6060": [], "6061": [], "6062": []}], "fault": true, "Leader": 8080, "publish_alert": [false, 0], "consumer_alert": [false, 0]}'
	file = open('settings.json', 'r')
	f = 0
	for count, line in enumerate(file):
		f+=1
	f+=1
	#f = count
	#print(count+1)
	file.close()
	file = open('settings.json', 'w')
	file.truncate(0)
	#file.close()
	i = 0
	while i<f:
		file.write(writer + '\n')
		i+=1
	file.close()
reset()
