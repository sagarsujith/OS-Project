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
