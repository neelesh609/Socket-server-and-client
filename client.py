# Name : Neelesh Shashidhar
# ID : 1001860682


from pydoc import Helper
import socket
import time  #import modules for client
FORMAT = "utf-8"
host_name = (socket.gethostname()) # host name of the client 

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # client socket family type and protocol
start = time.time()
c.connect(('localhost', 9999)) # connection parameters for client ip address and port number

print("Host Name of the Server is :", host_name)  # prints hostname
print("socket family, type and protocol is : ", c)  # prints client family type and protocol
print("socket fam is: ", c.family)
print("Socket type is :", c.type)
print("The protocol is:", c.proto) 
print('waiting for connections......') 



    
name = input("enter file name: ") # client requests for a file from server

c.send(name.encode(FORMAT)) # sends request to server

print(c.recv(1024).decode(FORMAT)) #recieves the file data from server
print('THE RTT is :  ', (time.time()-start)*100 // 100,' ms') # time from TCP request to recieving the file is Round trip time

