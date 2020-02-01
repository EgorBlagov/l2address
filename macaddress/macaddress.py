from .utils import clamp


def mac_address(value):
    return MacAddress(value)


MAX_HEXADECIMAL_DIGITS = 12


class MacAddress:
    def __init__(self, value):
        self.value = self._normalize_value(value)

    def _normalize_value(self, value):
        return clamp(value, self.max_value)

    @property
    def max_value(self):
        return pow(0x10, MAX_HEXADECIMAL_DIGITS) - 1

    def __str__(self):
        value_str = str(hex(self.value))[2:]
        full_mac_str = '0' * (MAX_HEXADECIMAL_DIGITS -
                              len(value_str)) + value_str
        split_by_colons = ':'.join([full_mac_str[2*i:2*i+2] for i in range(6)])
        return split_by_colons

    def __int__(self):
        return self.value

    def __add__(self, val):
        return MacAddress(self.value + val)

    def __radd__(self, val):
        return self + val
