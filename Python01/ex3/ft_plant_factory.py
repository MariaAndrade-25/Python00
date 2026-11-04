class Plant: 
	def __init__(self, name: str, age: int, height: float):
		self.name = name
		self.age = age
		self.height = height	
		
	def	grow(self, amount: float = 1.0)-> None:
		self.height += amount
		self.age += 1

	def display_info(self) -> None:
		print(f"{self.name}: {self.age} years, {round(self.height,1)} cm")

def main():
	plants = [
		Plant("Rose", 15, 12.5),
		Plant("Lilith", 25, 2.5),
		Plant("Sunflower", 10, 5.5),
		Plant("Devils Plant", 2, 1.5),
		Plant("Bonsai", 12, 45.8)
]
	print("=== Plant Factory Output ===")
	for plant in plants:
		plant.display_info()

	print("After Grown")
	plants[3].grow(5.5)
	plants[3].display_info()

if __name__== "__main__":
	main()
