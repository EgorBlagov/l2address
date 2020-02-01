# macaddress

Micro library I'm planing to develop by using TDD approach, just to try it.

## Example usage

```python

import macaddress

mac = macaddress.mac_address(0xff00ff)
print(mac)
# 00:00:00:ff:00:ff
mac += 0xff00
print(mac)
# 00:00:00:ff:ff:ff
mac -= macaddress.mac_address('00:00:00:ff:ff:f0')
print(mac)
# 00:00:00:00:00:0f
print(mac == macaddress.mac_address(0xf))
# True
print(macaddress.mac_address('ffffffffffff') + 1)
#00:00:00:00:00:00
```

## Features

At the current moment supports:

- Create MAC address from int
- Create MAC address from str
- Sum and Substitution of MAC addresses (and with ints)
- Convert MAC to string

## Plans

- Different formatting types (00:00:00:00:00:00, 0000.0000.0000, 00-00-00-00-00-00, and so on)
- Validation of format when parsing from string
- Multiplication by int
- Different lengths of MAC address (there are 64 bit MAC addesses I believe)
- Prepare as PyPi package (hence rename it, because there is a placeholder already)
