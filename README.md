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
  - Otherwise compute the tip as a `float` using whole-number percentages:  
    \[
    \text{tip} = \text{meal\_cost} \times \text{tip\_percent} \times 0.01
    \]
  - Return the computed tip.
 

- **`calculate_total(meal_cost, tip_amount)`**  
  - If invalid inputs, return `None`.  
  - Otherwise calculate the total bill using:  
    `total = meal_cost + tip_amount + (meal_cost * TAX_RATE)`  
  - Round the result to **2 decimal places** and return it.

You must import TAX_RATE

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
