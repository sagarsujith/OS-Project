# OS-Project
# Multi Threaded Proxy Server and Client
# Problem Statement
Develop a multi-threaded proxy server and client.The server accepts any URL from the client, 
fetches output, and returns to the client. The client should be able to save the output into an 
HTML page with an appropriate name.

# Abstract
The project is aimed at developing a multithreaded proxy server and client for the user. The 
major aim of this project is to prevent the client’s data from being used to browse the internet, 
instead a proxy the client is used to retrieve data from the server. This way provides more 
secure interaction between the client and the server.

In this project, the client is channeled through the proxy server running on localhost to 
the main server and the data retrieval takes place through it and the request is saved in the 
client’s workstation for later usage. It is multithreaded as a client can perform multiple searches 
at the same time and the proxy server can handle upto 5 and rest searches are executed after 
completion of the previous searches.

# Introduction
A proxy server is a computer system or router that functions as a relay between client and 
server. It helps prevent an attacker from invading a private network. Proxy Server retrieves data 
from the internet on behalf of the user. Normally when we open a web page in a browser it 
retrieves the data from the web server while in the case of a proxy server, when a proxy server 
receives a request from your computer then it retrieves the webpage on behalf of the user and 
sends it to the computer. Multiple requests can be handled by the proxy server 
simultaneously using multi-threading.. After making a request, on browser or from terminal, the 
files are temporarily stored in the cache directory in the proxy server. The next request for the 
same file will be faster because of this. Can be verified by timing the curl requests on the 
terminal.

Benefits of using a proxy server is that our IP address cannot be traced and the speed of 
retrieving data increases as the data retrieved will be stored in a cache database. If a proxy server 
is used by an organisation, then the organisation can also control the websites their employees 
access through the provided server.

By using the above concepts MultiThreading and Proxy-server, we made a secure 
environment for the browsing experience of the client. In the project, the client can provide the 
url once prompted by the terminal by using get function then the request is transported to proxy 
server, then in the proxy server a thread is created and html page for the same url is downloaded 
in the local machine as html file with suitable title. The proxy server is connected to a different 
port other than using a conventional port which is achieved by using socket programming in 
python language. Socket programming is a method of allowing two network nodes to converse 
with one another. One socket (node) listens on a specific port at an IP address, while the other 
socket establishes a connection with it. While the client connects to the server, the server creates 
the listener socket.

# Flow Chart
![image](https://user-images.githubusercontent.com/65555866/142754044-d3f0c536-2882-4f7c-8556-3018f661339d.png)
# OUTPUT
![image](https://user-images.githubusercontent.com/65555866/142754079-4bb3329e-8c7f-4c11-aa9b-bc8c33803c0e.png)
![image](https://user-images.githubusercontent.com/65555866/142754088-0764fc82-c5a8-4a8b-a158-cbe8b7d63fd2.png)
# Conclusion
In this project we developed a multithreaded proxy server which will accept urls from the client and will fetch the output for the following input URL as provided by the client. During the development of the project we made certain assumptions which are as follows :

●	We configured the proxy server such that it can listen upto 5 requests at a time and keeps creating 5 threads for each of these client requests, if any more requests are given the server goes into sleep mode for a certain period and then resumes processing requests.

●	We also developed the proxy server according to prototype needs so it accepts url requests in certain formats only which were mentioned in the input and output observations.

To achieve this proxy server and client we used python  programming language. While implementing this project we got familiarised with various libraries of python like sockets,os,sys,threading etc.. We got references from various websites for the practical implementation of this project. We also got familiarised with the socket programming concept.

