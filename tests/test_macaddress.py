import unittest
import macaddress


class test_MacAddress(unittest.TestCase):
    def test_create_from_int(self):
        result = macaddress.mac_address(0)
        self.assertIsNotNone(result)

    def test_mac_to_string(self):
        test_data = {
            0: '00:00:00:00:00:00',
            1: '00:00:00:00:00:01',
            10: '00:00:00:00:00:0a',
            0xff: '00:00:00:00:00:ff',
            0xaabbccdd: '00:00:aa:bb:cc:dd',
            0xffffffffffff: 'ff:ff:ff:ff:ff:ff'
        }

        for number, expected in test_data.items():
            mac = macaddress.mac_address(number)
            self.assertEqual(str(mac), expected,
                             'Number: {} (hex: {})'.format(number, hex(number)))

    def test_mac_exceed_input(self):
        test_data = {
            -1: 'ff:ff:ff:ff:ff:ff',
            -0xff: 'ff:ff:ff:ff:ff:01',
            0x1000000000000: '00:00:00:00:00:00',
            -0xffffffffffff: '00:00:00:00:00:01'
        }

        for number, expected in test_data.items():
            mac = macaddress.mac_address(number)
            self.assertEqual(str(mac), expected,
                             'Number (exceeding): {}'.format(number))

    def test_mac_max_value(self):
        mac = macaddress.mac_address(0)
        self.assertEqual(mac.max_value, 0xffffffffffff)

    def test_mac_to_int(self):
        test_data = {
            0: 0,
            1: 1,
            0xffff: 0xffff,
            0x1000000000000: 0,
            -1: 0xffffffffffff,
            -0xff: 0xffffffffff01
        }

        for number, expected in test_data.items():
            mac = macaddress.mac_address(number)
            self.assertEqual(int(mac), expected,
                             'Number: {} (hex: {})'.format(number, number))

    def test_mac_sum_with_int(self):
        self.assertEqual(int(macaddress.mac_address(0) + 1), 1)
        self.assertEqual(int(macaddress.mac_address(0xffffffffffff) + 1), 0)

    def test_mac_sum_int_with_mac(self):
        self.assertEqual(int(10 + macaddress.mac_address(0xff00)), 0xff0a)

    def test_mac_sum_with_mac(self):
        self.assertEqual(int(macaddress.mac_address(0xf) +
                             macaddress.mac_address(0xf0)), 0xff)

    def test_mac_sub_with_int(self):
        self.assertEqual(int(macaddress.mac_address(0) - 1), 0xffffffffffff)
        self.assertEqual(int(macaddress.mac_address(0xff) - 0xf), 0xf0)

    def test_mac_sub_int_with_mac(self):
        with self.assertRaises(TypeError):  # meaningless
            int(10 - macaddress.mac_address(0))

    def test_mac_sub_mac(self):
        self.assertEqual(int(macaddress.mac_address(0xff) -
                             macaddress.mac_address(0xf0)), 0xf)
        self.assertEqual(int(macaddress.mac_address(
            0) - macaddress.mac_address(1)), 0xffffffffffff)

    def test_default_constructor(self):
        self.assertEqual(int(macaddress.mac_address()), 0)

    def test_equality(self):
        self.assertEqual(macaddress.mac_address(0), macaddress.mac_address(0))
        self.assertEqual(macaddress.mac_address(
            0x1000000000000), macaddress.mac_address(0))
        self.assertNotEqual(macaddress.mac_address(),
                            macaddress.mac_address(0xff))

        self.assertNotEqual(macaddress.mac_address(), 0)
