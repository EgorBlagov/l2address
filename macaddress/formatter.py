from abc import ABC, abstractmethod
from .utils import per_join


class Formatter(ABC):
    def _to_clean_str(self, value, max_value):
        value_str = str(hex(value))[2:]
        full_mac_str = '0' * (len(hex(max_value)[2:]) -
                              len(value_str)) + value_str
        return full_mac_str

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
        raise NotImplementedError()


class PeriodFormatter(Formatter):
    def __init__(self, step=2):
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
