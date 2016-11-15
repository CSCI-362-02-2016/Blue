class x:
    def __init__(self, y):
        self.y = y

    def __eq__(self, other):
        return self.y == other.y
