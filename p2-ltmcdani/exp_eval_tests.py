# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    # postfix_eval

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)            # test addition

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")           # test invalid token

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")           # test insufficient operands

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")           # test too many operands

    def test_postfix_eval_05(self):
        self.assertAlmostEqual(postfix_eval("12 4 /"), 3)           # test division

    def test_postfix_eval_06(self):
        self.assertAlmostEqual(postfix_eval("5 4 *"), 20)           # test multiplication

    def test_postfix_eval_07(self):
        self.assertAlmostEqual(postfix_eval("99 1 -"), 98)           # test subtraction

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(postfix_eval("5 3  ^"), 125)           # test exponent

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval("2.2 4.5 *"), 9.9)            # test float

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval("5 3 + 2 ^ 36 6 / - 11 +"), 69)           # test combo

    def test_postfix_eval_11(self):
        self.assertAlmostEqual(postfix_eval("22 3 1 + /"), 5.5)         # test division resulting in float

    def test_postfix_eval_12(self):
        self.assertAlmostEqual(postfix_eval("-2 6 *"), -12)         # test negative values

    def test_postfix_eval_13(self):
        try:
            postfix_eval("8 0 /")
        except ValueError as e:
            self.assertEqual(str(e), "Cannot divide by 0")          # test division by zero catch

    # infix_to_postfix

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_0(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")            # test subtraction

    def test_infix_to_postfix_1(self):
        self.assertEqual(infix_to_postfix("6"), "6")            # test single value

    def test_infix_to_postfix_2(self):
        self.assertEqual(infix_to_postfix("6 ^ 2 - 1"), "6 2 ^ 1 -")            # test exponent 1

    def test_infix_to_postfix_3(self):
        self.assertEqual(infix_to_postfix("( 6 + 1 ) ^ 2"), "6 1 + 2 ^")            # test parenthesis

    def test_infix_to_postfix_4(self):
        self.assertEqual(infix_to_postfix("5 + 3 - 2"), "5 3 + 2 -")            # test addition and subtraction order of operations

    def test_infix_to_postfix_5(self):
        self.assertEqual(infix_to_postfix("1 * 3 / 4 - 1"), "1 3 * 4 / 1 -")            # test multiplication and division order of operations

    def test_infix_to_postfix_6(self):
        self.assertEqual(infix_to_postfix("4.0 * 3.0 - ( 1.2 + 3.3 ) / 4.0 + 8.1"), "4.0 3.0 * 1.2 3.3 + 4.0 / - 8.1 +")         # test float values

    def test_infix_to_postfix_7(self):
        self.assertEqual(infix_to_postfix("( -4 + 8 ) / 2 + -1"), "-4 8 + 2 / -1 +")            # test negative values

    # prefix_to_postfix

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_01(self):
        self.assertEqual(prefix_to_postfix("+ 5 6"), "5 6 +")           # test one operand

    def test_prefix_to_postfix_02(self):
        self.assertEqual(prefix_to_postfix("+ ^ 2 1 3"), "2 1 ^ 3 +")           # test two operands

    def test_prefix_to_postfix_03(self):
        self.assertEqual(prefix_to_postfix("- / 4 1 + 2 6 5"), "4 1 / 2 6 + -")         # test three operands

    def test_prefix_to_postfix_04(self):
        self.assertEqual(prefix_to_postfix("- 3.3 1.1"), "3.3 1.1 -")           # test floats

    def test_prefix_to_postfix_05(self):
        self.assertEqual(prefix_to_postfix("+ -4 3"), "-4 3 +")         # test negative numbers


if __name__ == "__main__":
    unittest.main()
