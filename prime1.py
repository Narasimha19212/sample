def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number
    # If a number 'num' has a divisor greater than its square root,
    # it must also have a divisor smaller than its square root.
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor, so it's not prime
    return True  # No divisors found, so it's prime

# Iterate from 1 to 100 and print prime numbers
print("Prime numbers from 1 to 100 are:")
for number in range(1, 101):
    if is_prime(number):
        print(number)