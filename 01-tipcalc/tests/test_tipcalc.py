import unittest
from unittest.mock import patch
import importlib
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tipcalc 
import config

class TestTipCalc(unittest.TestCase):

    # --- get_meal_cost tests ---
    def test_get_meal_cost_uses_prompt(self):
        with patch('builtins.input') as mock_input:
            prompt = "Enter meal cost: "
            tipcalc.get_meal_cost(prompt)
            mock_input.assert_called_once_with(prompt)

    def _num(self, entered, expected):
        with patch('builtins.input', return_value=entered):
            self.assertEqual(
                tipcalc.get_meal_cost("cost? "), expected,
                f'For input "{entered}" expected {expected}'
            )

    def test_get_meal_cost_valid(self):
        self._num("25", 25.0)

    def test_get_meal_cost_negative(self):
        self._num("-5", None)

    def test_get_meal_cost_non_number(self):
        self._num("goose", None)

    def test_get_meal_cost_empty(self):
        self._num("", None)

    # --- calculate_tip tests ---
    def test_calculate_tip_valid(self):
        self.assertEqual(tipcalc.calculate_tip(50, 20), 10.0)

    def test_calculate_tip_invalid(self):
        self.assertIsNone(tipcalc.calculate_tip(None, 15))

    # --- calculate_total tests ---
    def test_calculate_total_valid(self):
        # 50 meal + 10 tip + 50*0.07 tax = 63.5
        self.assertAlmostEqual(tipcalc.calculate_total(50, 10), 63.5, places=2)

    def test_calculate_total_invalid(self):
        self.assertIsNone(tipcalc.calculate_total(None, 5))

    # --- import/patch verification ---
    def test_import_tax_rate_patch(self):
        original = config.TAX_RATE
        try:
            with patch.object(config, 'TAX_RATE', 0.10):
                importlib.reload(tipcalc)
                self.assertEqual(tipcalc.TAX_RATE, 0.10)
                self.assertAlmostEqual(
                    tipcalc.calculate_total(100, 20), 130.0, places=2,
                    msg="Total not recalculated with patched TAX_RATE"
                )
        finally:
            with patch.object(config, 'TAX_RATE', original):
                importlib.reload(tipcalc)

if __name__ == '__main__':
    unittest.main()