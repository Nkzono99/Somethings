import math
import unittest

from sympy import isprime

from tmfunc import *


class TestTMFunc(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(3*2, mul(3, 2))
        self.assertEqual(2*3, mul(2, 3))

        self.assertEqual(10*1884, mul(10, 1884))

        self.assertEqual(0*3, mul(0, 3))
        self.assertEqual(3*0, mul(3, 0))

    def test_fact(self):
        for i in range(1, 11):
            self.assertEqual(math.factorial(i), fact(i))

    def test_fact_special(self):
        self.assertEqual(1, fact(0))

    def test_rem(self):
        def _assert(x, y):
            self.assertEqual(x % y, rem(x, y))
        _assert(10, 3)
        _assert(10, 2)
        _assert(2, 8)
        _assert(0, 7)

    def test_rem_special(self):
        self.assertEqual(0, rem(0, 0))
        self.assertEqual(0, rem(3, 0))
        self.assertEqual(0, rem(5, 0))
        self.assertEqual(0, rem(10, 0))

    def test_quo(self):
        def _assert(x, y):
            self.assertEqual(x//y, quo(x, y))

        _assert(6, 1)
        _assert(6, 2)
        _assert(6, 3)
        _assert(6, 6)
        _assert(10, 2)
        _assert(10, 5)

    def test_quo_special(self):
        self.assertEqual(0, quo(0, 0))
        self.assertEqual(0, quo(1, 0))
        self.assertEqual(0, quo(6, 0))
        self.assertEqual(0, quo(10, 0))

    def test_prime(self):
        def _assert(x):
            self.assertEqual(int(isprime(x)), prime(x))

        for x in range(2, 20):
            _assert(x)

    def test_prime_special(self):
        self.assertEqual(0, prime(0))
        self.assertEqual(0, prime(1))
