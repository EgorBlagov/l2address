from .utils import clamp
from .utils import parse_hex
from .formatter import COLON_FORMATTER


def mac_address(value=0):
    return MacAddress(value)


MAX_HEXADECIMAL_DIGITS = 12


class MacAddress:
    def __init__(self, value):
        self.value = self._normalize_value(value)

    def _normalize_value(self, value):
        if isinstance(value, str):
            value_int = parse_hex(value)
        elif isinstance(value, MacAddress):
            value_int = value.value
        else:
            value_int = value

        return clamp(value_int, self.max_value)

    @property
    def max_value(self):
        return pow(0x10, MAX_HEXADECIMAL_DIGITS) - 1

    def to_str(self, formatter=COLON_FORMATTER):
        return formatter.format(self.value, self.max_value)

    def __str__(self):
        return self.to_str()

    def __int__(self):
        return self.value

    def __add__(self, val):
        return MacAddress(self.value + int(MacAddress(val)))

    def __radd__(self, val):
        return self + val

    def __sub__(self, val):
        return self + int(MacAddress(val))*(-1)

    def __eq__(self, rhs):
        return isinstance(rhs, MacAddress) and self.value == rhs.value

    def __hash__(self):
        return hash(self.value)
