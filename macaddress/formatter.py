import re
from abc import ABC, abstractmethod

from .utils import parse_hex, per_join


class FormatterLibrary:
    def __init__(self):
        self.formatters = []

    @property
    def default_formatter(self):
        return self.formatters[0]

    def register(self, formatter):
        if formatter not in self.formatters:
            self.formatters.append(formatter)

    def parse(self, _str, max_value):
        for each in self.formatters:
            try:
                return each.parse(_str, max_value)
            except ValueError:
                pass

        raise ValueError('Invalid MAC format')


FORMATTER_LIBRARY = FormatterLibrary()


class Formatter(ABC):
    def __init__(self):
        FORMATTER_LIBRARY.register(self)

    def _to_clean_str(self, value, max_value):
        value_str = str(hex(value))[2:]
        full_mac_str = '0' * (self._hex_digits_count(max_value) -
                              len(value_str)) + value_str
        return full_mac_str

    def _hex_digits_count(self, value):
        return len(hex(value)[2:])

    def _common_regex(self, delimeter, step):

    @abstractmethod
    def format(self, value, max_value):
        pass

    @abstractmethod
    def parse(self, _str, max_value):
        pass


class ColonFormatter(Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), ':', 2)

    def parse(self, _str, max_value):
        m = re.match(per_join(
            [r'[\da-fA-f]' for _ in range(self._hex_digits_count(max_value))], r'\:', 2), _str)

        if m is None:
            raise ValueError('Invalid MAC format')
        else:
            return parse_hex(_str)


class PeriodFormatter(Formatter):
    def __init__(self, step=2):
        super().__init__()
        self.step = step

    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '.', self.step)

    def parse(self, _str, max_value):
        raise NotImplementedError()


class HyphenFormatter(Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '-', 2)

    def parse(self, _str, max_value):
        raise NotImplementedError()


class CleanFormatter(Formatter):
    def format(self, value, max_value):
        return self._to_clean_str(value, max_value)

    def parse(self, _str, max_value):
        raise NotImplementedError()


COLON_FORMATTER = ColonFormatter()
PERIOD_FORMATTER = PeriodFormatter()
HYPHEN_FORMATTER = HyphenFormatter()
PERIOD_TRIPLET_FORMATTER = PeriodFormatter(3)
PERIOD_QUADRIPLET_FORMATTER = PeriodFormatter(4)
CLEAN_FORMATTER = CleanFormatter()
