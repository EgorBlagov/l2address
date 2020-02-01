import unittest
import macaddress


class test_macaddress_str(unittest.TestCase):
    def test_mac_from_str(self):
        test_data = [
            '00:00:00:00:00:00',
            'aa:bb:cc:dd:ee:ff',
            '00:aa:00:bb:00:cc'
        ]

        for data in test_data:
            self.assertEqual(str(macaddress.mac_address(data)),
                             data, 'String: {}'.format(data))
