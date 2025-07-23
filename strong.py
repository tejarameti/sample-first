import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.
    """
    original_num = num
    sum_of_factorials = 0
    temp_num = num

    while temp_num > 0:
        digit = temp_num % 10
        sum_of_factorials += math.factorial(digit)
        temp_num //= 10

    return sum_of_factorials == original_num

def find_strong_numbers_in_range(start, end):
    """
    Finds and prints all strong numbers within a specified range.
    """
    print(f"Strong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_strong_number(number):
            print(number)

# Call the function to find strong numbers between 1 and 5000
find_strong_numbers_in_range(1, 5000)