import unittest

from macaddress.utils import clamp, parse_hex, per_join


class test_utils(unittest.TestCase):
    def test_clamp_limits(self):
        self.assertEqual(clamp(0, 1), 0)
        self.assertEqual(clamp(1, 0xff), 1)
        self.assertEqual(clamp(0xff + 1, 0xff), 0)
        self.assertEqual(clamp(0xff + 1, 0xff), 0,)
        self.assertEqual(clamp(0xff + 1 + 5, 0xff), 5)
        self.assertEqual(clamp(0xff + 1 + 0xff + 1 + 5, 0xff), 5)
        self.assertEqual(clamp(-1, 0xff), 0xff)
        self.assertEqual(clamp(-0xf, 0xff), 0xf1)
        self.assertEqual(clamp(-0x100, 0xff), 0)

    def test_parse_hex(self):
        test_data = {
            '10': 0x10,
            'aa:bb': 0xaabb,
            'aa-bb-cc': 0xaabbcc,
            'abcDEF': 0xabcdef
        }
        for _str, expected in test_data.items():
            self.assertEqual(parse_hex(_str), expected,
                             'String: {}'.format(_str))

    def test_per_join(self):
        self.assertEqual(per_join('abc', ':'), 'a:b:c')
        self.assertEqual(per_join('abc', ':', 3), 'abc')
        self.assertEqual(per_join('abc', ':', 2), 'ab:c')
        self.assertEqual(per_join('aaaabbbbcc', '.', 4), 'aaaa.bbbb.cc')
        self.assertEqual(per_join('', 'aaaa'), '')
        self.assertEqual(per_join('abcde', '0ab', 2), 'ab0abcd0abe')

    def test_per_join_iterible(self):
        self.assertEqual(
            per_join(['abc', 'def', 'bbb', 'aaa'], '-', 2), 'abcdef-bbbaaa')
