import socket
import os


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 40000))
clientSocket.send(bytes(input('Command: '), 'utf-8'))
server_message = clientSocket.recv(4096)
clientSocket.close()
print(str(server_message, 'utf-8'))


