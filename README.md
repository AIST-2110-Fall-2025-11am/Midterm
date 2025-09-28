# Midterm: Tip & Tax Calculator

This midterm assignment will help you practice creating and using functions to
structure your code efficiently. You will build a small program that calculates
the cost of a meal with tip and tax included.

## Learning Objectives

1. Develop functions to handle calculations and input validation.
2. Structure programs using multiple functions and clear early returns.
3. Practice working with user inputs, conditional logic, and exception handling.
4. Use constants from a local file and math operations from a built-in library.
5. Test programs to ensure correct functionality and handle invalid inputs gracefully.

## Assignment Structure

The assignment is contained in the folder:

- `tipcalc/`

Inside you will find:
- `config.py` — defines the constant `TAX_RATE`
- `tipcalc.py` — starter code with functions to complete

## What You Will Do

You must implement three functions in `tipcalc.py`:

- **`get_meal_cost(prompt)`**  
  - Prompt the user, try to convert their input into a `float`.  
  - If valid and ≥ 0, return the value.  
  - Otherwise return `None`.

- **`calculate_tip(meal_cost, tip_percent)`**  
  - If `meal_cost` is invalid (`None` or < 0), return `None`.  
  - Otherwise compute the tip as a `float` and return it.  

- **`calculate_total(meal_cost, tip_amount)`**  
  - If invalid inputs, return `None`.  
  - Otherwise calculate the total bill using:  
    `total = meal_cost + tip_amount + (meal_cost * TAX_RATE)`  
  - Round the result to **2 decimal places** and return it.

You must import TAX_RATE & math

## Example Runs

```
Enter meal cost: 50
Enter tip percent: 20
Tip: 10.0
Total with tax: 56.50
```

```
Enter meal cost: goose
Enter tip percent: 15
Invalid input. Please enter a valid meal cost.
```

---

## Grading Rubric

* `get_meal_cost` correctness & prompt use – **25%**
* `calculate_tip` correctness – **25%**
* `calculate_total` correctness (tax + tip + rounding) – **30%**
* Proper imports (`math`, `TAX_RATE`), clean early returns, no loops – **20%**


## test_tipcalc.py

```python
import unittest
from unittest.mock import patch
import tipcalc
import config
import importlib

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
```

---

This keeps the **same structure and skills** as your first midterm (triangle), but framed around **meal cost, tip, and tax**.

Do you want me to also prepare a **student-facing quick-start snippet** (like showing exactly where to replace the `...` placeholders in `tipcalc.py`) so it mirrors the handholding level of your triangle README?
