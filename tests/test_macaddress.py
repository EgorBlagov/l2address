import unittest
import macaddress


class test_MacAddress(unittest.TestCase):
    def test_create_from_int(self):
        result = macaddress.mac_address(0)
        self.assertIsNotNone(result)
