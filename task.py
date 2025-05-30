class Task:
    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.status = "PENDING"  # PENDING, RUNNING, SUCCESS, FAILED
        self.error = None
        self.result = None

    def run(self):
        if self.status == "SUCCESS":
            return self.result
        self.status = "RUNNING"
        try:
            self.result = self.func()
            self.status = "SUCCESS"
        except Exception as e:
            self.error = e
            self.status = "FAILED"
            raise
