import os
import socket
import subprocess

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 40000))
serverSocket.listen(5)

while True:
    conn, addr = serverSocket.accept()
    message = ''
    while True:
        data = conn.recv(4096)
        if not data: 
            break
        message += str(data, 'utf-8')
        out = subprocess.check_output(str(message).split(), stderr=subprocess.STDOUT)
        conn.send(out)
    conn.close()
    



