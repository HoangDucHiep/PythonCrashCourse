class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
        
minh = Dog('Minh', 1)
print(f"My dog called {minh.name} is {minh.age} year old.")
print("I tell him to sit down: ")
minh.sit()
print("And he rolls over")
minh.roll_over()
