import producer
import time

producer.publish("Charan ", "Topic", 5050)
time.sleep(10)
producer.publish("Charan Loves Football", "Message", 5051)
time.sleep(10)
producer.publish("Pradyuman", "Topic", 5050)
time.sleep(10)
producer.publish("Pradyuman is a cricketer", "Message", 5052)
time.sleep(10)
producer.publish("Charan and Pradyuman are sportsman", "Message", 5050)
