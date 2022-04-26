from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight=50, fuel=20, fuel_consumption=2):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
        if not self.started:
            raise LowFuelError

    def move(self, distance):
        fuel_needed = self.fuel_consumption*distance
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel("Not enough fuel")