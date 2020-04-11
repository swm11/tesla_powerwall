from typing import Union

def convert_to_kwh(value, rounded=True):
    """Converts watt hours to kilo watt hours and optionally round the value"""
    temp = value / 1000
    if rounded:
        return round(temp, 1)
    else:
        return temp