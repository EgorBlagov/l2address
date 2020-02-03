from .formatter import DEFAULT_FORMATTERS
from .utils import clamp, parse_hex


def mac_address(value=0, formatter=DEFAULT_FORMATTERS[0]):
    return MacAddress(value, formatter)


MAX_HEXADECIMAL_DIGITS = 12


class MacAddress:
    def __init__(self, value, formatter):
        self.formatter = formatter
        self.value = self._normalize_value(value)

    def _normalize_value(self, value):
        if isinstance(value, str):
            value_int = self._parse(value)
        elif isinstance(value, MacAddress):
            value_int = value.value
        elif isinstance(value, int):
            value_int = value
        else:
            raise ValueError('Invalid value to create MAC address')

        return clamp(value_int, self.max_value)

    @property
    def max_value(self):
        return pow(0x10, MAX_HEXADECIMAL_DIGITS) - 1

    def to_str(self, formatter=None):
        if formatter is None:
            formatter = self.formatter

        return formatter.format(self.value, self.max_value)

    def _parse(self, value_str):
        for each in [self.formatter] + DEFAULT_FORMATTERS:
            try:
                return each.parse(value_str, self.max_value)
            except ValueError:
                pass

        raise ValueError('Invalid MAC address format')

    def __str__(self):
        return self.to_str()

    def __int__(self):
        return self.value

    def __add__(self, val):
        return MacAddress(self.value + int(MacAddress(val, self.formatter)), self.formatter)

    def __radd__(self, val):
        return self + val

    def __sub__(self, val):
        return self + int(MacAddress(val, self.formatter))*(-1)

    def __eq__(self, rhs):
        return isinstance(rhs, MacAddress) and self.value == rhs.value

    def __hash__(self):
        return hash(self.value)
