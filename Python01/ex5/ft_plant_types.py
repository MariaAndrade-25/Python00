class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = float(height)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = int(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def grow(self, amount: float = 1.0) -> None:
        self.set_height(self._height + amount)

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self._name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow_and_age(self, height_growth: float, days: int) -> None:
        self.grow(height_growth)
        self.set_age(self._age + days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()

    print("[asking the rose to bloom]")
    flower.bloom()

    print("\n=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()

    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April")
    vegetable.show()

    print("[make tomato grow and age for 20 days]")
    vegetable.grow_and_age(42.0, 20)
    vegetable.show()


if __name__ == "__main__":
    main()