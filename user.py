class User:
    def __init__(self, nickname="Anonymous"):
        self.nickname = nickname

    def __repr__(self):
        return f"[{self.nickname}]"

    def __eq__(self, other):
        return isinstance(other, User) and self.nickname == other.nickname

    def __hash__(self):
        return hash(self.nickname)
