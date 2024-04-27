```python
import socket
import threading
from PyQt5.QtCore import pyqtSignal, QObject

class CollaborationManager(QObject):
    """
    Manages real-time collaboration features including communication and file sharing among users.
    """
    message_received = pyqtSignal(str)
    file_received = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.host = 'localhost'
        self.port = 5000
        self.clients = []
        self.server_socket = None
        self.running = False

    def start_server(self):
        """
        Starts the collaboration server to allow real-time communication and file sharing.
        """
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen()
            self.running = True
            print("Collaboration Server Started on port", self.port)
            threading.Thread(target=self.accept_connections).start()
        except Exception as e:
            print("Error starting server:", e)

    def accept_connections(self):
        """
        Accepts incoming connections from clients.
        """
        while self.running:
            client, address = self.server_socket.accept()
            self.clients.append(client)
            print(f"Connected to {address}")
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        """
        Handles communication with connected clients.
        """
        while self.running:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    print("Received:", message)
                    self.message_received.emit(message)
                    self.broadcast_message(message, client)
            except Exception as e:
                print("Error handling client:", e)
                self.clients.remove(client)
                break

    def broadcast_message(self, message, sender):
        """
        Broadcasts a message to all clients except the sender.
        """
        for client in self.clients:
            if client is not sender:
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print("Error broadcasting message:", e)
                    self.clients.remove(client)

    def send_file(self, file_path, client):
        """
        Sends a file to a specified client.
        """
        try:
            with open(file_path, 'rb') as file:
                data = file.read()
                client.send(data)
                print(f"Sent file {file_path} to client.")
                self.file_received.emit(file_path)
        except Exception as e:
            print("Error sending file:", e)

    def stop_server(self):
        """
        Stops the collaboration server and disconnects all clients.
        """
        self.running = False
        for client in self.clients:
            client.close()
        self.server_socket.close()
        print("Collaboration Server Stopped")

```
