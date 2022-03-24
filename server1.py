# Name : Neelesh Shashidhar
# ID : 1001860682

import socket
from _thread import *
import time                                                      #import modules for socket 
SIZE = 1024              
FORMAT = "utf-8"

host_name = (socket.gethostname())                               # gethostname gives us the name of the servers host.

def threading_proc(c, addr):                                     # function for multithreading
    print(f"{addr} connected. ")
    name = c.recv(1500).decode(FORMAT)                           # The server recieves the file request

    if name.startswith("GET /"):                                 # loop to segregate webbrowser request and local client request
        try:
            
            filename = name.split()[1]                           # reading the file data to display on web browser.
            file = open(filename[1:])
            file_data = file.read()

            c.send("HTTP/1.1 200 OK\r\n\r\n".encode(FORMAT))     # sending the HTTP request web browser.

            for items in range(0, len(file_data)):  
                c.send(file_data[items].encode(FORMAT))          # reading the data into empty string file_data to print.

            c.send("\r\n".encode(FORMAT))
            


        except IOError:
        
            c.send("HTTP/1.1 404 Not found\r\n\r\n".encode(FORMAT))  # in case the file is not found 404 error is given.
            c.send("<html><head></head><body><h1>404 Not found</h1></body></html>\r\n".encode(FORMAT))
            c.close()                                            # connection will be closed for the wrong request.
    else:
        
        file_data = ""  
        
        start_time = time.time()                                 # time when the file enters 
        print("The Time in is : ", (start_time)/1000000000, "ms")
        print("connected with", addr)
        print(name)
        
        try:
            file = open(name, 'r')                              # reads the file local client.
            for data in file:
                file_data = file_data + data                     # appending the data to string file_data
            c.sendall(file_data.encode())                        # sending the file data to client side
            endtime = time.time() 
            total = (endtime-start_time)                         # total time from request to file out.
            print("Timeout is : ", (endtime)/1000000000, "ms")   # timeout 
            print("Total time in server is: ", total, "ms")
            
            
        except IOError:
            print("404 file not found")                          # error if file is not found
            



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # socket type and family.
    print('Socket Created') 
   
except socket.error as err:                                     # in case socket is not initialized error is thrown.
    print("socket creation failed !!")

s.bind(('localhost', 9999))                                     #binds the localhost ip and the port number

s.listen()                                                      # sockets starts listening to the clients

while True:
    
    print("Host Name of the Client is :", host_name)            # host name of the client
    
    print("The Socket family, type and protocol is : ", s )     # printing the socket modules
    print("The Socket family is : ", s.family)                  # socket family 
    print("The Socket type is : SOCK_STREAM ", s.type)          # socket type
    print("The Protocol is", s.proto)                           # socket protocol
    print('waiting for connections......') 
    
    c, addr = s.accept()                                        # server accepts the connection.
    start_new_thread(threading_proc, (c, addr))                 # calling the multithreading function.

                                                   