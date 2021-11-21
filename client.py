import socket
import os
import re
import sys

OUTPUT = r"C:\os-multi-threaded-proxy-server\client-html-responses"

class Client:
    def __init__(self):
        self.client_socket = socket.socket()
        self.client_socket.connect(('localhost', 5050))
        pass
    def send_to_proxy(self, request_url, OUTPUT=OUTPUT):
        self.client_socket.send(bytes('%s'%request_url, 'utf-8'))
        domain_name = re.search("http[s]?:[/][/]?(www)?[.]?(.*)\.", request_url).group(2)
        html_content = self.client_socket.recv(1024).decode()
        html_file = open(OUTPUT+'\%s_response.html'%domain_name, "w")
        html_file.write(html_content)
        html_file.close()
        print("Check the html_file saved in %s\\%s_response.html"%(OUTPUT, domain_name))


if __name__ == "__main__":
    print("Enter exit to stop\n")
    while True:
        reqs = input().split(" ")
        if reqs[0] == "exit":
            break
        else:
            count = 0
            for req in reqs[1:]:
                if count>=5:
                    print("Currently the proxy server is working for maximum clients and hence sleeping for few seconds before further process")
                    time.sleep(5)
                    count = 0
                cln = Client()
                cln.send_to_proxy(req)
                count += 1
                
        
        
