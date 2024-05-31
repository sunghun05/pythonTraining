# server.py
# type: ignore
 
import socket
import threading

HOST = 'localhost'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Connected by', addr)
data = ''
def pr_msg():
    while 1:
        data = conn.recv(1024)
        if data: print(data,upper())

thread_1 = threading.Thread(target=pr_msg, args=(''))
thread_1.start()

while 1:
    send_data = input("enter data : ")
    if send_data[:4] in ['quit', 'Quit', 'QUIT']:
        conn.send('Server Quit')
        threading.exit()
        conn.close()
    conn.send('Server: '+send_data)