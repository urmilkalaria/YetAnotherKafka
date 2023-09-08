#!/usr/bin/python3

import subprocess
import time
subprocess.Popen(['gnome-terminal', '-e', "python3 broker.py"])
time.sleep(2)
subprocess.Popen(['gnome-terminal', '-e', "python3 consumer.py"])
time.sleep(2)
subprocess.Popen(['gnome-terminal', '-e', "python3 producer.py"])
