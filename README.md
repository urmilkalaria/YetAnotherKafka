# BD project


## 📝 Table of Contents

- Settings
- Producer
- Broker
- Consumer
- Zookeeper
- Usage


### Settings(config)

- Settings json file will contain state of broker which help in establishing and maintaining all the connections across the architecture.
- It contains flags, ports and other information for achieving proper functioning. This file can be accessed by all members in the architecture and uses it to communicate with each other.

### Producer 

- Producer can either create a topic or send message to the topic whose structure can be found in main file.
- When ever producer sends a topic or message to the broker it alerts the broker by changig in config file after the alert an socket connection is opened for the sending of the data to broker.
- Threading was avoided as due to multiple requests conflicts were found.
- So instead of connection were opened and closed accordingly with each message for there to be no conflicts

### Broker 

- Right now the 3 brokers are created statically. One of the 3 brokers is the leader broker

- The leader broker handles all the publish operations,consume operations, it also distributes topics among other brokers in a round robin fashion.
- Currently 3 publishers are present in the architecture.
- The other broker remain dormant and wait for the connection from consumer to know when to send data according to the topic it is subscribed to.

### Consumer 

- Consumer can subscribe to a certain topic to recieve messsages from that topic.

- These consumer listen forever and recieve messages from topic via socket connection with broker publishers whenever broker receives message from producers of that topic they send the approcriate message with help of config file state.

### Zookeeper 

- Zookeeper monitors all broker and sees which broker is running or not by polling.
- It checks all ports running and by shell commands checks if the ports are used by the architecture or are blocked by other application.
- Zookeeper also can replace these ports
- Zookeeper also assigns a new leader if the leader broker has failed.
- All the changes are reflected on the config file
- It saves the log of the state into log.txt and resets all settings.json
