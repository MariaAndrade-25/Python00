class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Defaulting height to 0.0cm")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Defaulting age to 0 days")
        else:
            self._age = age

        print(f"Plant created: {self.name}: {self._height:.1f}cm, "
              f"{self._age} days old")

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height) if self._height.is_integer() else self._height}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def display_info(self) -> None:
        print(f"Current state: {self.name}: {self._height:.1f}cm, "
              f"{self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-10)

    plant.display_info()


if __name__ == "__main__":
    main()