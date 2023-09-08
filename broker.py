import client
import json
import os
import time
import server
import zookeeper

with open('settings.json', 'r+') as f:
    settings = json.load(f)

def create_broker(PORT):
    settings["broker_port"][0].append({str(PORT): {}})

global temp_msg_Queue
global temp_topic_Queue

temp_msg_Queue = []
temp_topic_Queue = []

os.remove('settings.json')
with open('settings.json', 'w') as f:
    json.dump(settings, f)

def Process_1():
    while True:
        with open('settings.json', 'r+') as f:
            global settings
            settings = json.load(f)

        if settings["publish_alert"][0]:
            s = str(client.client(settings["publish_alert"][1],settings["Leader"]))
            s = s.split(',')
            if s[0] == 'Message':
                if s[1] not in temp_msg_Queue:
                    temp_msg_Queue.append(s[1])
            elif s[0] == 'Topic':
                if s[1] not in temp_topic_Queue:
                    temp_topic_Queue.append(s[1])
            share_topics_among_brokers(settings=settings)
            share_messages_among_brokers(settings=settings)
            # os.remove('settings.json')
            # with open('settings.json', 'w') as f:
            #     json.dump(settings, f)
        time.sleep(15)
    
def share_topics_among_brokers(settings):
    
    k = len(settings['broker_port'][0].keys())
    for i in range(len(temp_topic_Queue)):
        if i%k == 0:
            if temp_topic_Queue[i] not in settings['broker_port'][0]["8080"].keys():
                settings['broker_port'][0]["8080"][temp_topic_Queue[i]] = []
        elif i%k == 1:
            if temp_topic_Queue[i] not in settings['broker_port'][0]["8081"].keys():
                settings['broker_port'][0]["8081"][temp_topic_Queue[i]] = []
        else:
            if temp_topic_Queue[i] not in settings['broker_port'][0]["8082"].keys():
                settings['broker_port'][0]["8082"][temp_topic_Queue[i]] = []

def share_messages_among_brokers(settings):
    
    flag = 0
    k = len(settings['broker_port'][0].keys())
    for i in range(len(temp_msg_Queue)):
        for j in temp_msg_Queue[i].split():
            for k in settings['broker_port'][0].keys():
                for l in settings['broker_port'][0][k].keys():
                    if j in l:
                        settings['broker_port'][0][k][l].append(temp_msg_Queue[i])
                        send_to_consumer(l, l + ',' +temp_msg_Queue[i])
                        flag = 1
                        break
                if flag:
                    break
            if flag:
                flag = 0
                break

def send_to_consumer(Topic, message):
    snd_port = settings["Leader"]
    recv_port = []
    flag = 0
    for i in settings["broker_port"][0].keys():
        for j in settings["broker_port"][0][i].keys():
            if j == Topic:
                snd_port = int(i)
                flag = 1
                break
        if flag:
            break
    
    for i in settings["consumer_port"][0].keys():
        if Topic in settings["consumer_port"][0][i]:
            recv_port.append(i)
    
    settings["consumer_alert"][0] = True
    settings["consumer_alert"][1] = snd_port
    settings["publish_alert"][0] = False
    settings["publish_alert"][1] = 0
    os.remove('settings.json')
    with open('settings.json', 'w') as f:
        json.dump(settings, f)
    
    for i in recv_port:
        server.server(snd_port, message)
        time.sleep(10)
while True:
    try:
        Process_1()
    except:
        pass