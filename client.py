# Commit made by Dhruv Sharma, SRN: PES1UG20CS129
import socket

def client(server_port, client_port):
 
    # Create a socket object
    s = socket.socket()        
    
    # Define the port on which you want to connect             
    s.bind(('', client_port))
    # connect to the server on local computer
    s.connect(('127.0.0.1', server_port))
    
    # receive data from the server and decoding to get the string.
    msg = (s.recv(1024).decode())
    # close the connection
    s.close()    

    return msg
