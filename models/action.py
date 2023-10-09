class Action:
    def __init__(self, type: str, value: int = None, message: str = None):
        self.type = type
        self.value = value
        self.message = message

    def __str__(self):
        return f"Action(type={self.type}, value={self.value}, message={self.message})"
