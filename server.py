import os
import socket
import subprocess

ADDRESS = socket.gethostname()
PORT = 25009



serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ADDRESS, PORT))
serverSocket.listen(5)

while True:
    conn, addr = serverSocket.accept()
    message = ''
    
    
    while True:
        data = conn.recv(4096)

        if not data: 
            break
        message += str(data, 'utf-8')
        out = subprocess.run(message.split(), capture_output=True)
        exit = bool(out.returncode)
        if exit == False:
            conn.send(out.stdout)
        else:
            conn.send(out.stderr)
        
    conn.close()
    



