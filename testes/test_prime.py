# -*- coding: utf-8 -*-
import unittest

from prime import is_prime


class IsPrimeTestCase(unittest.TestCase):

    def test_should_return_True_to_prime_numbers(self):
        self.assertTrue(is_prime(5))

    def test_should_return_False_to_non_prime_numbers(self):
        self.assertFalse(is_prime(8))

    def test_should_not_consider_all_odd_numbers_to_be_prime(self):
        self.assertFalse(is_prime(45))

    def test_should_raise_ValueError_for_strings(self):
        self.assertRaises(ValueError, is_prime, "45")
