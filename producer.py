import server
import json
import os

with open('settings.json', 'r+') as f:
    global settings
    settings = json.load(f)


def create_producer(port):
    settings["publisher_port"].append(port)

def validate(port):
    if port in settings["publisher_port"]:
        return True
    else:
        return False


def publish(message, type, PORT):
    if type == 'Topic':
        parsed_msg = str()
        parsed_msg += type + ',' + message
    else:
        parsed_msg = str()
        parsed_msg += 'Message' + ',' + message
    if validate(PORT):
        settings["publish_alert"][0] = True
        settings["publish_alert"][1] = PORT
        os.remove('settings.json')
        with open('settings.json', 'w') as f:
            json.dump(settings, f)
        if parsed_msg != None:
            server.server(PORT, parsed_msg)