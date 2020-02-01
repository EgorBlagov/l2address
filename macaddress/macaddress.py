
def mac_address(value):
    return MacAddress(value)


MAX_HEXADECIMAL_DIGITS = 12


class MacAddress:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        value_str = str(self.value)
        full_mac_str = '0' * (MAX_HEXADECIMAL_DIGITS -
                              len(value_str)) + value_str
        split_by_colons = ':'.join([full_mac_str[2*i:2*i+2] for i in range(6)])
        return split_by_colons
