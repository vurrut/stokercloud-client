from enum import Enum


class NotConnectedException(Exception):
    pass


class PowerState(Enum):
    ON = 1
    OFF = 0


class Unit(Enum):
    KWH = 'kwh'
    PERCENT = 'pct'
    DEGREE = 'deg'
    KILO_GRAM = 'kg'
    GRAM = 'g'


class Value:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit


class ControllerData:
    def __init__(self, data):
        if data['notconnected'] != 0:
            raise NotConnectedException("Furnace/boiler not connected to StokerCloud")

        self.alarm = {
            0: PowerState.OFF,
            1: PowerState.ON
        }.get(data['miscdata'].get('alarm'))

        self.running = {
            0: PowerState.OFF,
            1: PowerState.ON
        }.get(data['miscdata'].get('running'))