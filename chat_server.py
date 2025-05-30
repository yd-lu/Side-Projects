import socket
import threading

class ChatServer:
    def __init__(self, host='127.0.0.1', port=9000):
        self.host = host
        self.port = port
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((self.host, self.port))
        self.server_sock.listen(100)

        self.clients = {}       # socket -> nickname
        self.nick_to_sock = {}  # nickname -> socket

    def start(self):
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_sock, addr = self.server_sock.accept()
            nickname = client_sock.recv(1024).decode()
            self.clients[client_sock] = nickname
            self.nick_to_sock[nickname] = client_sock
            print(f"Client {nickname} connected from {addr}")
            threading.Thread(target=self.handle_client, args=(client_sock,), daemon=True).start()

    def handle_client(self, client_sock):
        try:
            while True:
                msg = client_sock.recv(1024).decode()
                if msg.startswith("["):
                    parts = msg.split(" ", 1)
                    self.broadcast(client_sock, parts[1])
                elif msg.startswith("/msg"):
                    parts = msg.split(" ", 2)
                    if len(parts) == 3:
                        self.send_private_message(client_sock, parts[1], parts[2])
        except:
            pass
        finally:
            self.disconnect(client_sock)

    def broadcast(self, sender_sock, msg, exclude=None):
        for sock in self.clients:
            if sock != exclude:
                full = f"[{self.clients[sender_sock]} -> All] {msg}"
                try:
                    sock.send(full.encode())
                except:
                    pass

    def send_private_message(self, sender_sock, target_nick, message):
        target_sock = self.nick_to_sock.get(target_nick)
        if target_sock:
            full = f"[{self.clients[sender_sock]} -> You] {message}"
            try:
                target_sock.send(full.encode())
            except:
                pass

    def disconnect(self, client_sock):
        if client_sock not in self.clients:
            return
        nick = self.clients[client_sock]
        print(f"Client '{nick}' disconnected.")
        del self.clients[client_sock]
        del self.nick_to_sock[nick]
        self.broadcast(client_sock, f"{nick} has left the chat.")
        client_sock.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start()
