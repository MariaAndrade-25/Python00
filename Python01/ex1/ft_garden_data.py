class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 20.5, 5)
    sunflower = Plant("Sunflower", 15, 4)
    devils_plant = Plant("Devils Plant", 40, 30)
    rose.show()
    sunflower.show()
    devils_plant.show()
