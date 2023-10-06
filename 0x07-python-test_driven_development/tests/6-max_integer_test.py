#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ok lets go"""
    def test_a(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_b(self):
        self.assertEqual(max_integer([1, 5, 55, 6, 20, 2, 11]), 55)

    def test_c(self):
        self.assertEqual(max_integer([1, 5, 5, 55, 6, 20, 2, 2, 11, 1]), 55)

    def test_c(self):
        self.assertEqual(max_integer([1, 5, 55, 0, 20, 2, 0]), 55)

    def test_d(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_e(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_f(self):
        self.assertEqual(max_integer([3]), 3)

    def test_g(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_h(self):
        self.assertEqual(max_integer([-1, -5, -55, -6, -20, -2, -11]), -1)

    def test_i(self):
        self.assertEqual(max_integer(
            [-1, -5, -5, -55, -6, -20, -2, -2, -11, -1]), -1
            )

    def test_j(self):
        self.assertEqual(max_integer([-1, -5, -55, -0, -20, -2, 0]), 0)

    def test_k(self):
        self.assertEqual(max_integer([-3, -3, -3, -3]), -3)

    def test_l(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_l2(self):
        self.assertEqual(max_integer([-3]), -3)

    def test_m(self):
        self.assertEqual(max_integer(
            [-1, 5, -5, 55, -6, 20, -2, 2, -11, -1]), 55
            )

    def test_n(self):
        self.assertEqual(max_integer([1, -5, 55, 0, 20, -2, 0]), 55)

    def test_o(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_p(self):
        self.assertEqual(max_integer([1, float('inf'), 3, 4, 5]), float('inf'))

    def test_q(self):
        self.assertEqual(max_integer([1, -float('inf'), 5, 4, 6]), 6)

    def test_r(self):
        self.assertEqual(max_integer([]), None)

    def test_s(self):
        self.assertEqual(max_integer(), None)

    def test_t(self):
        self.assertEqual(max_integer("str"), "t")

    def test_u(self):
        self.assertEqual(max_integer((1, 5, 55, 6, 20, 2, 11)), 55)

    def test_v(self):
        self.assertEqual(max_integer([None]), None)

    def test_w(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "3", 4])

    def test_x(self):
        self.assertRaises(TypeError, max_integer, 2)

    def test_y(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_z(self):
        self.assertRaises(TypeError, max_integer, [None, 1, 2, 3, 4])

    def test_yrte(self):
        self.assertRaises(TypeError, max_integer, [1, 2, 3, 4], 5)

    def test_likj(self):
        self.assertRaises(TypeError, max_integer, {1, 2, 3, 4})