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
            self.assertEqual(str(mac), expected)
