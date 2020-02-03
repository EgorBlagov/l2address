import re
import unittest

import l2address


class TestMacFormatter(l2address.Formatter):
    def format(self, value, max_value):
        pattern = ':0{}d'.format(len(str(max_value)))
        return 'DEC-{{{}}}'.format(pattern).format(value)

    def _get_validator_regexp(self, _str, max_value):
        return r'^DEC\-\d{{{}}}$'.format(len(str(max_value)))

    def _parse_value_from_str(self, _str):
        clean_decimal = ''.join(x.group(0) for x in re.finditer(r'\d', _str))
        return int(clean_decimal)


class test_CustomFormatter(unittest.TestCase):
    def test_format_is_invalid(self):
        with self.assertRaisesRegex(ValueError, 'Invalid MAC address'):
            l2address.mac_address('DEC-000000000000123')

    def test_format_is_valid_with_formatter(self):
        self.assertEqual(int(l2address.mac_address(
            'DEC-000000000000123', TestMacFormatter())), 123)

    def test_format_default_with_custom_formatter(self):
        mac = l2address.mac_address('DEC-000000000012345', TestMacFormatter())
        self.assertEqual(str(mac), 'DEC-000000000012345')

    def test_format_to_different_format(self):
        mac = l2address.mac_address('DEC-000000000012345', TestMacFormatter())
        self.assertEqual(mac.to_str(
            l2address.HyphenFormatter()), '00-00-00-00-30-39')

    def test_validate_invalid(self):
        with self.assertRaisesRegex(ValueError, 'Invalid MAC address'):
            l2address.mac_address('dec-121212', TestMacFormatter())

    def test_sum_with_custom_string(self):
        self.assertEqual(str(l2address.mac_address(
            'DEC-000000000000123', TestMacFormatter()) + 'DEC-000000000000100'), 'DEC-000000000000223')
