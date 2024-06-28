import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

cliens = []
nicknames = []

def broadcast(message):
       for client in cliens:
              client.send(message)

def handle_client(client):
       while True:
              try:
                     message = client.recv(1024)
                     broadcast(message)
              except:
                     index = cliens.index(client)
                     cliens.remove(client)
                     client.close()
                     nickname = nicknames[index]
                     broadcast(f"{nickname} Left the Chat!".encode('utf-8'))
                     nicknames.remove(nickname)
                     break
def receive():
       while True:
              client, address = server.accept()
              print(f"Connected with {str(address)}")

              client.send('NICK'.encode('utf-8'))
              nickname = client.recv(1024).decode('utf-8')
              nicknames.append(nickname)
              cliens.append(client)

              print(f"Nickname of the clients is {nickname}")
              broadcast(f"{nickname} joined the chat!".encode('utf-8'))
              client.send('Connected to the server!'.encode('utf-8'))

              thread = thread.Threading(target=handle_client, args=(client,))
              thread.start()

print('server is listening')
receive()