# Terminal Chat Application

A simple terminal-based chat server and client system using Python sockets and threading. Includes basic features such as public broadcasting, private messages, and custom commands using decorators.

## Features

- Multi-client support via threads
- Public broadcasting
- Private messaging (`/msg <user> <message>`)
- Nickname changes (`/nick <newname>`)
- Command parser with decorator-based extensibility
- Graceful disconnection (`/quit`)

## How to Run

### Start the Server

```bash
python chat_server.py
```

### Start the Client (in separate terminals)

```bash
python chat_client.py
```
