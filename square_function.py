# The function to be tested
def square_num(a):
    if isinstance(a, str):
        raise ValueError("Input must be a number (integer or float).")
    return a*a