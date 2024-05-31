#client

import socket # type: ignore
import threading

HOST = 'localhost'
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = ''

def pr_msg():
    while 1:
        data = s.recv(1024)
        if data: print(data.upper())
    
thread_1 = threading.Thread(target=pr_msg, args=(''))
thread_1.start()

while 1:
    send_data = input("enter data : ")
    if send_data in ['quit', 'Quit', 'QUIT']:
        s.send('Client Quit')
        threading.exit()
        s.close()
    s.send('Client: '+send_data)