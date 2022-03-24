Name : Neelesh Shashidhar
ID : 1001860682

1) The zipped folder consists of server1.py file , client.py file and 2 textfiles:
The text files being:
a)RobertFrost.txt 
b)Neel.txt

2) First we unzip the folder and open the folder in any editor of choice (vs-code recommended).

3) First run the server1.py file and once it says waiting for connection:
   
   we can request the file in 2 ways:

   a) Through a browser: type localhost:9000/"filename" file name will be the file that you want to request.
   b) Run the client.py file, it will ask user input for the file. the file name has to be enetered

4) In the first case the browser will retrieve the data of the filename given in the url extension.

5) In the second case the data of the file requested by the client will be diplayed on the client side.

6) all the specifications such as RTT, Timeout etc have been displyed on the server as well as the client side as specified.

7)Packages required: import socket , from _thread import * , import time.  

REFERENCES:

1) python skeleton reference from modules - canvas.
2) https://stackoverflow.com/questions/55661915/how-to-close-a-socket-connection-in-python
3) https://internalpointers.com/post/making-http-requests-sockets-python
4) https://www.youtube.com/watch?v=u4kr7EFxAKk - socket programming tutorial
5) https://www.tutorialspoint.com/python-program-to-calculate-the-round-trip-time-rtt
6) https://www.studytonight.com/network-programming-in-python/socket-methods 