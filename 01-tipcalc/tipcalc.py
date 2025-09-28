
# 1) Complete this function
def get_meal_cost(prompt: str) -> float | None:
    """
    Prompt for a float. Return the value if >= 0.
    On any failure (ValueError, empty input, negative), return None.
    """
    ...


# 2) Complete this function
def calculate_tip(meal_cost: float, tip_percent: float) -> None | float:
    """
    Return tip amount as float.
    If invalid inputs, return None.
    """
    ...


# 3) Complete this function
def calculate_total(meal_cost: float, tip_amount: float):
    """
    Return total bill as float rounded to 2 decimals:
        meal_cost + tip_amount + (meal_cost * TAX_RATE)
    Return None if inputs invalid.
    """
    ...


def main():
    cost = get_meal_cost("Enter meal cost: ")
    if cost is None:
        print("Invalid input. Please enter a valid meal cost.")
        return

    try:
        tip_percent = float(input("Enter tip percent: "))
    except ValueError:
        print("Invalid input. Please enter a number for tip percent.")
        return

    tip = calculate_tip(cost, tip_percent)
    if tip is None:
        print("Could not calculate tip.")
        return
    print(f"Tip: {tip}")

    total = calculate_total(cost, tip)
    if total is None:
        print("Could not calculate total.")
        return
    print(f"Total with tax: {total:.2f}")


if __name__ == "__main__":
    main()
