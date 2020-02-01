import unittest
import macaddress


class test_MacAddress(unittest.TestCase):
    def test_create_from_int(self):
        result = macaddress.mac_address(0)
        self.assertIsNotNone(result)

    def test_mac_to_string(self):
        mac = macaddress.mac_address(0)
        self.assertEqual(str(mac), '00:00:00:00:00:00')
