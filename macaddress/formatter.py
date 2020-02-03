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

        raise ValueError('Invalid MAC address format')


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

    def _common_regex(self, max_value, delimeter, step):
        return "^" + per_join([r'[\da-fA-f]' for _ in range(self._hex_digits_count(max_value))], delimeter, step) + "$"

    @abstractmethod
    def format(self, value, max_value):
        pass

    def parse(self, _str, max_value):
        m = re.match(self._get_validator_regexp(_str, max_value), _str)
        if m is None:
            raise ValueError('Invalid MAC address format')
        else:
            return parse_hex(_str)

    @abstractmethod
    def _get_validator_regexp(self, _str, max_value):
        pass


class ColonFormatter(Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), ':', 2)

    def _get_validator_regexp(self, _str, max_value):
        return self._common_regex(max_value, r'\:', 2)


class PeriodFormatter(Formatter):
    def __init__(self, step=2):
        super().__init__()
        self.step = step

    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '.', self.step)

    def _get_validator_regexp(self, _str, max_value):
        return self._common_regex(max_value, r'\.', self.step)


class HyphenFormatter(Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '-', 2)

    def _get_validator_regexp(self, _str, max_value):
        return self._common_regex(max_value, r'\-', 2)


class CleanFormatter(Formatter):
    def format(self, value, max_value):
        return self._to_clean_str(value, max_value)

    def _get_validator_regexp(self, _str, max_value):
        return self._common_regex(max_value, '', 2)


COLON_FORMATTER = ColonFormatter()
PERIOD_FORMATTER = PeriodFormatter()
HYPHEN_FORMATTER = HyphenFormatter()
PERIOD_TRIPLET_FORMATTER = PeriodFormatter(3)
PERIOD_QUADRIPLET_FORMATTER = PeriodFormatter(4)
CLEAN_FORMATTER = CleanFormatter()
