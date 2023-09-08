import client
import json
import os
import time

with open('settings.json', 'r+') as f:
    settings = json.load(f)

def create_consumer(PORT):
    settings['consumer_port'][0][str(PORT)].append(PORT)

global temp_msg_Queue
temp_msg_Queue = []

os.remove('settings.json')
with open('settings.json', 'w') as f:
    json.dump(settings, f)

def subscribe_topics(topic_name, PORT):
    with open('settings.json', 'r+') as f:
        global settings
        settings = json.load(f)
    
    if topic_name not in settings["consumer_port"][0][str(PORT)]:
        settings["consumer_port"][0][str(PORT)].append(topic_name)
    
    os.remove('settings.json')
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def check(tag, port):
    if tag in settings["consumer_port"][0][str(port)]:
        return True
    else:
        return False

def Process(PORT):
    while True:
        with open('settings.json', 'r+') as f:
            global settings
            settings = json.load(f)
        
        if settings["consumer_alert"][0]:
            s = str(client.client(settings["consumer_alert"][1],PORT))
            s = s.split(',')
            if check(s[0], PORT):
                print(s[1])
                temp_msg_Queue.append(s)
        
        settings["consumer_alert"][0] = False
        settings["consumer_alert"][1] = 0
        os.remove('settings.json')
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        time.sleep(10)

subscribe_topics("Pradyuman", 6060)
subscribe_topics("Charan", 6061)

while True:
    try:
        Process(6060)
    except:
        time.sleep(10)
        pass