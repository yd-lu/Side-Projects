class CommandParser:
    def __init__(self):
        self._cmds = {}

    def __call__(self, msg, context):
        if not msg.startswith("/"):
            return False
        parts = msg.split(" ", 1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        if cmd in self._cmds:
            self._cmds[cmd](args, context)
        else:
            print(f"Invalid command: {cmd}")
        return True

    def register(self, cmd):
        def decorator(fn):
            self._cmds[cmd] = fn
            return fn
        return decorator
