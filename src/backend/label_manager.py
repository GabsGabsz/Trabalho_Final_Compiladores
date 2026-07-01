class LabelManager:
    def __init__(self):
        self.counter = 0

    def new(self, prefix: str = "L") -> str:
        label = f"{prefix}_{self.counter}"
        self.counter += 1
        return label