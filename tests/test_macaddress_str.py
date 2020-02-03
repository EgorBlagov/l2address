import unittest

import macaddress


class test_macaddress_str(unittest.TestCase):
    def test_mac_from_str(self):
        test_data = {
            '00:00:00:00:00:00': '00:00:00:00:00:00',
            'aa:bb:cc:dd:ee:ff': 'aa:bb:cc:dd:ee:ff',
            '00:aa:00:bb:00:cc': '00:aa:00:bb:00:cc',
            'aa-bb-cc-dd-ee-ff': 'aa:bb:cc:dd:ee:ff',
            'aa.bb.cc.dd.ee.ff': 'aa:bb:cc:dd:ee:ff',
            'aabbccddeeff': 'aa:bb:cc:dd:ee:ff',
            'aab.bcc.dde.eff': 'aa:bb:cc:dd:ee:ff',
            'aabb.ccdd.eeff': 'aa:bb:cc:dd:ee:ff',
            'aAbBCCddeeff': 'aa:bb:cc:dd:ee:ff'
        }

        for data, expected in test_data.items():
            self.assertEqual(str(macaddress.mac_address(data)),
                             expected, 'String: {}'.format(data))

    def test_mac_invalid_str_format(self):
        test_data = [
            '00-aa-bb',
            '00:aa:bb.ccddee',
            'xaxbxaxbxaxbxaxb',
            '-10-10-10-10',
            '-1503',
            'aabbccddeeffaa',  # too long hence invalid
        ]

        for data in test_data:
            with self.assertRaisesRegex(ValueError, r'Invalid MAC address format', msg="String: {}".format(data)):
                macaddress.mac_address(data)

    def test_mac_string_format_style(self):
        self.assertEqual(macaddress.mac_address().to_str(),
                         '00:00:00:00:00:00')
        self.assertEqual(macaddress.mac_address().to_str(
            macaddress.COLON_FORMATTER), '00:00:00:00:00:00')
        self.assertEqual(macaddress.mac_address().to_str(
            macaddress.PERIOD_FORMATTER), '00.00.00.00.00.00')
        self.assertEqual(macaddress.mac_address().to_str(
            macaddress.HYPHEN_FORMATTER), '00-00-00-00-00-00')
        self.assertEqual(macaddress.mac_address().to_str(
            macaddress.PERIOD_TRIPLET_FORMATTER), '000.000.000.000')
        self.assertEqual(macaddress.mac_address().to_str(
            macaddress.PERIOD_QUADRIPLET_FORMATTER), '0000.0000.0000')
        self.assertEqual(macaddress.mac_address().to_str(
            macaddress.CLEAN_FORMATTER), '000000000000')

    def test_sum_with_str(self):
        self.assertEqual(macaddress.mac_address() +
                         '00:00:00:00:ff:00', macaddress.mac_address(0xff00))

        self.assertEqual(macaddress.mac_address(0xffffffffffff) +
                         '00:00:00:00:00:01', macaddress.mac_address())

    def test_sub_with_str(self):
        self.assertEqual(macaddress.mac_address() -
                         '00:00:00:00:00:ff', macaddress.mac_address(0xffffffffff01))
        self.assertEqual(macaddress.mac_address(0xffff) -
                         '00:00:00:00:00:ff', macaddress.mac_address(0xff00))

    def test_sum_and_sub_with_invalid_str(self):
        test_data = [
            'abc',
            '-1-2-3-',
            '-ffaabb',
            'abcd.abcd.aa:bb',
        ]

        for _str in test_data:
            with self.assertRaisesRegex(ValueError, r'Invalid MAC address format'):
                macaddress.mac_address() + _str

            with self.assertRaisesRegex(ValueError, r'Invalid MAC address format'):
                macaddress.mac_address() - _str
