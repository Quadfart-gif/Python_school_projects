#game 
class Car:
    def __init__(self, make, model, year, color):
        # Initialize the car's attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0  # The car starts at a speed of 0

    def accelerate(self, increment):
        # Increase the speed of the car
        self.speed += increment
        print(f"The car has accelerated. Current speed: {self.speed} km/h")

    def brake(self, decrement):
        # Decrease the speed of the car, but it won't go below 0
        self.speed = max(0, self.speed - decrement)
        print(f"The car has braked. Current speed: {self.speed} km/h")

    def display_info(self):
        # Display the car's details
        print(f"Car Info: {self.year} {self.make} {self.model}, Color: {self.color}, Speed: {self.speed} km/h")

# Example of how to use the class
my_car = Car("Toyota", "Corolla", 2020, "Red")
my_car.display_info()
my_car.accelerate(30)
my_car.brake(10)
my_car.display_info()



#If you see this, you have succeeded!
