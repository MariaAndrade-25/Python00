class Plant:
    class System:
        def __init__(self):
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0
            self.__shade_calls = 0

        def record_grow(self):
            self.__grow_calls += 1

        def record_age(self):
            self.__age_calls += 1

        def record_show(self):
            self.__show_calls += 1

        def record_shade(self):
            self.__shade_calls += 1

        def display(self, name):
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self.__grow_calls} grow, "
                f"{self.__age_calls} age, "
                f"{self.__show_calls} show"
            )

        def display_shade(self):
            print(f"{self.__shade_calls} shade")

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age_days = age
        self.__system = Plant.System()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount):
        self.height += amount
        self.__system.record_grow()

    def age(self, days):
        self.age_days += days
        self.__system.record_age()

    def show(self):
        self.__system.record_show()
        print(
            f"{self.name}: {self.height:.1f}cm, "
            f"{self.age_days} days old"
        )

    def display_statistics(self):
        self.__system.display(self.name)


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )
        self._Plant__system.record_shade()

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def display_statistics(self):
        super().display_statistics()
        self._Plant__system.display_shade()


class Seed(Flower):
    def __init__(self, name, height, age, color, seeds=0):
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def bloom(self):
        super().bloom()
        self.seeds = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant):
    plant.display_statistics()


print("=== Garden statistics ===")

print("=== Check year-old")
print(
    "Is 30 days more than a year? ->",
    Plant.is_older_than_year(30)
)
print(
    "Is 400 days more than a year? ->",
    Plant.is_older_than_year(400)
)

print("=== Flower")
rose = Flower("Rose", 15.0, 10, "red")
rose.show()
display_statistics(rose)

print("[asking the rose to grow and bloom]")
rose.grow(8.0)
rose.bloom()
rose.show()
display_statistics(rose)

print("=== Tree")
oak = Tree("Oak", 200.0, 365, 5.0)
oak.show()
display_statistics(oak)

print("[asking the oak to produce shade]")
oak.produce_shade()
display_statistics(oak)

print("=== Seed")
sunflower = Seed("Sunflower", 80.0, 45, "yellow")
sunflower.show()

print("[make sunflower grow, age and bloom]")
sunflower.grow(30.0)
sunflower.age(20)
sunflower.bloom()
sunflower.show()
display_statistics(sunflower)

print("=== Anonymous")
anonymous = Plant.create_anonymous()
anonymous.show()
display_statistics(anonymous)
