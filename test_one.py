"""End-to-end tests for the restaurant billing command-line program."""

import subprocess
import sys
import unittest
from pathlib import Path


PROGRAM = Path(__file__).with_name("one.py")


def run_program(user_input):
    return subprocess.run(
        [sys.executable, str(PROGRAM)],
        input=user_input,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


class BillingProgramTests(unittest.TestCase):
    def test_regular_bill(self):
        output = run_program("Dosa\n2\nIdli\n3\nTea\n2\nbill\n")
        self.assertIn("Subtotal: 320.00", output)
        self.assertIn("Discount: 0.00", output)
        self.assertIn("GST(5%): 16.00", output)
        self.assertIn("Grand Total: 336.00", output)

    def test_discount_applies_above_500(self):
        output = run_program("Thali\n4\nbill\n")
        self.assertIn("Subtotal: 600.00", output)
        self.assertIn("Discount: 60.00", output)
        self.assertIn("GST(5%): 27.00", output)
        self.assertIn("Grand Total: 567.00", output)

    def test_no_discount_at_exactly_500(self):
        output = run_program("Thali\n2\nDosa\n2\nIdli\n1\nbill\n")
        self.assertIn("Subtotal: 500.00", output)
        self.assertIn("Discount: 0.00", output)
        self.assertIn("GST(5%): 25.00", output)
        self.assertIn("Grand Total: 525.00", output)

    def test_invalid_quantities_are_rejected(self):
        output = run_program("Dosa\nabc\nDosa\n0\nDosa\n1\nbill\n")
        self.assertIn("Invalid quantity. Enter a whole number.", output)
        self.assertIn("Invalid quantity. Enter a number greater than 0.", output)
        self.assertIn("Grand Total: 84.00", output)

    def test_unknown_item_is_rejected(self):
        output = run_program("Pizza\nTea\n1\nbill\n")
        self.assertIn("Item not on menu. Available: Dosa, Idli, Thali, Tea", output)
        self.assertIn("Grand Total: 21.00", output)

    def test_empty_cart(self):
        output = run_program("bill\n")
        self.assertIn("Cart is empty!", output)
        self.assertNotIn("Grand Total:", output)


if __name__ == "__main__":
    unittest.main()
