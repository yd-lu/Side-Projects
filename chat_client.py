import socket
import threading
from user import User
from command_parser import CommandParser

class ChatClient:
    def __init__(self, user, host='127.0.0.1', port=9000):
        self.user = user
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

        self.parser = CommandParser()
        self.register_commands()

    def start(self):
        self.sock.send(self.user.nickname.encode())
        threading.Thread(target=self.receive_loop, daemon=True).start()
        self.send_loop()

    def send_loop(self):
        while True:
            msg = input("> ").strip()
            if msg.startswith("/"):
                handled = self.parser(msg, context=self)
                if handled:
                    continue
            full_msg = f"[{self.user.nickname}] {msg}"
            self.sock.send(full_msg.encode())

    def receive_loop(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode()
                if not msg:
                    print("Disconnected from server.")
                    break
                print(msg)
            except ConnectionResetError:
                print("Server closed connection.")
                break

    def register_commands(self):
        @self.parser.register("/nick")
        def change_nickname(args, client):
            new_nick = args.strip()
            if not new_nick:
                print("Usage: /nick <nickname>")
                return
            old_nick = client.user.nickname
            client.user.nickname = new_nick
            print(f"Nickname changed from {old_nick} to {new_nick}")

        @self.parser.register("/msg")
        def private_message(args, client):
            parts = args.split(" ", 1)
            if len(parts) < 2:
                print("Usage: /msg <user> <message>")
                return
            target, message = parts
            payload = f"/msg {target} {message}"
            client.sock.send(payload.encode())

        @self.parser.register("/quit")
        def quit(args, client):
            print("Goodbye!")
            client.sock.close()
            exit(0)

if __name__ == "__main__":
    nickname = input("Your nickname: ") or "Anonymous"
    user = User(nickname)
    client = ChatClient(user)
    client.start()
