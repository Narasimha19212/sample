import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    A strong number is a number whose sum of the factorial of its digits 
    equals the number itself.
    """
    if num < 0:
        return False  # Strong numbers are typically defined for non-negative integers
    
    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10

    return sum_of_factorials == original_num

def find_strong_numbers_in_range(start, end):
    """
    Finds and prints all strong numbers within a specified range.
    """
    print(f"Strong numbers between {start} and {end}:")
    found_strong_numbers = []
    for i in range(start, end + 1):
        if is_strong_number(i):
            found_strong_numbers.append(i)
    
    if found_strong_numbers:
        print(found_strong_numbers)
    else:
        print("No strong numbers found in this range.")

# Example usage: Find strong numbers from 1 to 5000
find_strong_numbers_in_range(1, 5000)