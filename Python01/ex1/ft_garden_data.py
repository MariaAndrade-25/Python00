class Plant:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")



if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 20, 5.3)
    sunflower = Plant("Sunflower", 15, 4)
    devilsplant = Plant("Devils Plant", 40, 30)
    rose.show()
    sunflower.show()
    devilsplant.show()