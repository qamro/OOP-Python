# the composed engine directly owns its components, so we can just use the default destructor

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)  # Composition: Car has an Engine
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]  # Composition: Car has Wheels
        
    def display_info(self):
        print(f"Car: {self.make} {self.model}")
        print(f"Engine Horse Power: {self.engine.horse_power}")
        print("Wheels:")
        for wheel in self.wheels:
            print(f"- Size: {wheel.size}")
            
            
# Example usage
my_car = Car("Renault", "Clio Classique", 200, 16)

my_car.display_info()