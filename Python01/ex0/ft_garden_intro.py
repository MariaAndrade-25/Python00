class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm,")

        if self.age >= 1:
            age_text = f"{self.age} " + ("days old" if self.age > 1 else "day old")
        else:
            age_text = "just planted"
        print(age_text)

list_of_plants = {
    0: {"name": "Rose", "height": 25.0, "age": 1},
    1: {"name": "Lilith", "height": 15.0, "age": 20},
    2: {"name": "Sunflower", "height": 10.4, "age": 15},
    3: {"name": "Devils Plant", "height": 5.0, "age": 5}
}
    
def main():
    print("=== Welcome to My Garden ===")
    for p in list_of_plants:
        plant = list_of_plants[p]
        plants = Plant(plant["name"], plant["height"], plant["age"])
        plants.show()


if __name__ == "__main__":
    main()