import random
import time

class WearableDeviceSimulator:
    def __init__(self):
        self.heart_rate = 70  # starting heart rate
        self.speed = 0
        self.movement = {"x": 0, "y": 0, "z": 0}

    def generate_data(self):
        # Simulate data changes over time
        self.heart_rate = random.randint(60, 180)
        self.speed = round(random.uniform(0, 12), 2)  # speed in km/h
        self.movement = {
            "x": random.uniform(-1, 1),
            "y": random.uniform(-1, 1),
            "z": random.uniform(-1, 1)
        }
        return {
            "heart_rate": self.heart_rate,
            "speed": self.speed,
            "movement": self.movement
        }

    def start_simulation(self, duration=60):
        for _ in range(duration):
            data = self.generate_data()
            print("Simulated Data:", data)
            time.sleep(1)  # simulate real-time data generation
