from __future__ import absolute_import, print_function

from devices import init_gpio


fan_instance = None
def get_fan_instance():
    return fan_instance

class FourSpeedRealayFan:
    def __init__(self, pin0, pin1, pin2, pin3):
        init_gpio()
        global fan_instance
        self.current_speed = 0
        fan_instance = self

    def select_speed(self, speed):
        assert speed >= 0 and speed <= 3
        self.current_speed = speed

    @property
    def max_speed(self):
        return 3

