import unittest
from macaddress.utils import clamp


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
