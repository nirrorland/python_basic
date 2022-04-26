"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(TypeError):
    pass


class NotEnoughFuel(TypeError):
    pass


class CargoOverload(TypeError):
    pass
