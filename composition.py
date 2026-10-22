# the composed engine directly owns its components, so we can just use the default destructor

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    pass

class Car:
    pass