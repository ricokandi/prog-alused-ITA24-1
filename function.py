"""Function examples."""


# func()
def func():
    """Print info."""
    print("I´m inside the function")


# my_name_is(name)
def my_name_is(name: str):
    """Print introduction."""
    print(f"My name is {name}")


# sum_six(num)
def sum_six(num: int) -> int:
    """Return sum + 6."""
    return num + 6


# sum_numbers()
def sum_numbers(a: int, b: int):
    """Return sum of 2 numbers."""
    return a + b


# usd_to_eur()
def usd_to_eur(a: int):
    """Convert USD to EUR."""
    return a * 0.8