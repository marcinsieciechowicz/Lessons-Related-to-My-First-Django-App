class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print('getting value')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < 273:
            raise ValueError('Temperature below -273 is impossible to reach')
        print('Setting value')
        self._temperature = value



