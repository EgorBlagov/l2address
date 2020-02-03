# l2address

Micro library I'm planing to develop by using TDD approach, just to try it.

## Example usage

```python

import l2address

mac = l2address.mac_address(0xff00ff)
print(mac)
# 00:00:00:ff:00:ff
mac += 0xff00
print(mac)
# 00:00:00:ff:ff:ff
mac -= l2address.mac_address('00:00:00:ff:ff:f0')
print(mac)
# 00:00:00:00:00:0f
print(mac == l2address.mac_address(0xf))
# True
print(l2address.mac_address('ffffffffffff') + 1)
# 00:00:00:00:00:00
print(l2address.mac_address(0xff, l2address.PeriodFormatter(4)))
# 0000.0000.00ff
```

## Features

At the current moment supports:

- Create MAC address from int
- Create MAC address from str
- Sum and Substitution of MAC addresses (and with ints)
- Convert MAC to string
- Different formatting types (00:00:00:00:00:00, 0000.0000.0000, 00-00-00-00-00-00, and so on)
- Validation of format when parsing from string. There are predefined formats, but can be extended, see: [Extending Formats](#extending-formats)

## Extending Formats

```python
import l2address
from l2address.utils import per_join

# Just inherit l2address.Formatter and use new formatter


class MyMacStarFormatter(l2address.Formatter):
    def format(self, value, max_value):
        return per_join(self._to_clean_str(value, max_value), '*', 2)

    def _get_validator_regexp(self, _str, max_value):
        return r'^([\da-fA-F][\da-fA-F]\*?){6}'


try:
    l2address.mac_address('AB*ab*bc*de*ff*ff')
except ValueError:
    print('Failed as expected')
    # Failed as expected

mac = l2address.mac_address('AB*ab*bc*de*ff*ff', MyMacStarFormatter())
print(mac)
# ab*ab*bc*de*ff*ff
print(mac.to_str(l2address.ColonFormatter()))
# ab:ab:bc:de:ff:ff
print(l2address.mac_address(0xff).to_str(MyMacStarFormatter()))
# 00*00*00*00*00*ff
```

## Plans

- Multiplication by int
- Different lengths of MAC address (there are 64 bit MAC addesses I believe)
