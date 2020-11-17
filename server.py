import socket
import time
import _thread
from utils import *

#server configurations
server_ip = socket.gethostname()
server_port = 12345
MAX_USERS = 32

# import databases


#CLI
def home_page(username, client_socket):
    #TODO add CLI for homepage here
    return

#client thread

def client_thread(client_socket, address):
    user = authenticate(client_socket) #TODO write code for authenticate in utils
    #TODO mark user as online
    home_page(user, client_socket) #TODO write code for home_page 
    #TODO mark user as offline
    print(f"Closing client thread: {address}")
    client_socket.send("Thanks for using Tweeter. See you soon!")
    client_socket.shutdown(2)
    client_socket.close()
    return

#create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(MAX_USERS)

print("Server started and listening...")

while True:
    client_socket, address = server_socket.accept()
    print(f"New client connected: {address}")

    _thread.start_new_thread(client_thread, (client_socket, address))

    