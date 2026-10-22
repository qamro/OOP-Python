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
        self.wheels = Wheel(wheel_size)  # Composition: Car has Wheels