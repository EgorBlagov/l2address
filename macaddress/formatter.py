from .utils import per_join


class Formatter:
    def _to_clean_str(self, value, max_value):
        value_str = str(hex(value))[2:]
        full_mac_str = '0' * (len(hex(max_value)[2:]) -
                              len(value_str)) + value_str
        return full_mac_str

    def format(self, value, max_value):
        pass

    def parse(self, _str, max_value):
        pass


class ColonFormatter(Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), ':', 2)


class PeriodFormatter(Formatter):
    def __init__(self, step=2):
        self.step = step

    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '.', self.step)


class HyphenFormatter(Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '-', 2)


class CleanFormatter(Formatter):
    def format(self, value, max_value):
        return self._to_clean_str(value, max_value)


COLON_FORMATTER = ColonFormatter()
PERIOD_FORMATTER = PeriodFormatter()
HYPHEN_FORMATTER = HyphenFormatter()
PERIOD_TRIPLET_FORMATTER = PeriodFormatter(3)
PERIOD_QUADRIPLET_FORMATTER = PeriodFormatter(4)
CLEAN_FORMATTER = CleanFormatter()
