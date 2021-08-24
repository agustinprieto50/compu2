import socket
import os


ADDRESS = socket.gethostname()
PORT = 25009

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((ADDRESS, PORT))
while True:

    command = bytes(input('Command: '), 'utf-8')
    
    if command == 'exit':
        break
    
    clientSocket.send(command)

    server_message = clientSocket.recv(4096)
    clientSocket.close()
    print(str(server_message, 'utf-8'))
