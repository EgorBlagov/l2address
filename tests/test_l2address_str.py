import unittest

import l2address


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
            self.assertEqual(str(l2address.mac_address(data)),
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
                l2address.mac_address(data)

    def test_mac_string_format_style(self):
        self.assertEqual(l2address.mac_address().to_str(),
                         '00:00:00:00:00:00')
        self.assertEqual(l2address.mac_address().to_str(
            l2address.ColonFormatter()), '00:00:00:00:00:00')
        self.assertEqual(l2address.mac_address().to_str(
            l2address.PeriodFormatter()), '00.00.00.00.00.00')
        self.assertEqual(l2address.mac_address().to_str(
            l2address.HyphenFormatter()), '00-00-00-00-00-00')
        self.assertEqual(l2address.mac_address().to_str(
            l2address.PeriodFormatter(3)), '000.000.000.000')
        self.assertEqual(l2address.mac_address().to_str(
            l2address.PeriodFormatter(4)), '0000.0000.0000')
        self.assertEqual(l2address.mac_address().to_str(
            l2address.CleanFormatter()), '000000000000')

    def test_sum_with_str(self):
        self.assertEqual(l2address.mac_address() +
                         '00:00:00:00:ff:00', l2address.mac_address(0xff00))

        self.assertEqual(l2address.mac_address(0xffffffffffff) +
                         '00:00:00:00:00:01', l2address.mac_address())

    def test_sub_with_str(self):
        self.assertEqual(l2address.mac_address() -
                         '00:00:00:00:00:ff', l2address.mac_address(0xffffffffff01))
        self.assertEqual(l2address.mac_address(0xffff) -
                         '00:00:00:00:00:ff', l2address.mac_address(0xff00))

    def test_sum_and_sub_with_invalid_str(self):
        test_data = [
            'abc',
            '-1-2-3-',
            '-ffaabb',
            'abcd.abcd.aa:bb',
        ]

        for _str in test_data:
            with self.assertRaisesRegex(ValueError, r'Invalid MAC address format'):
                l2address.mac_address() + _str

            with self.assertRaisesRegex(ValueError, r'Invalid MAC address format'):
                l2address.mac_address() - _str
