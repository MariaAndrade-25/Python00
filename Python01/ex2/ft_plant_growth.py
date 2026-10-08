class Plant:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        