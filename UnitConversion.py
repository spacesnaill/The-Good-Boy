
#TODO import Pint, a library for unit conversion
#TODO add a function to convert units
#this may get rolled into the bot.py file rather than being a seperate class, I haven't decided yet

import pint

class UnitConversion:

    def __init__(self):
        self.unit_registry = pint.UnitRegistry()

    def convert_units(self, amount, input_unit, output_unit):
        source = '{} * {}'.format(amount, input_unit)
        destination = output_unit
        return self.unit_registry(source).to(destination)