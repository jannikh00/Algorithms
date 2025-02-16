# Assignment 4: Recursive Solutions

# This python file contains four functions that use a recursive approach
# Each function is described by a docstring

def factorial(num):
    """
    Recursively computes the factorial of a given number.

    The factorial of a non-negative integer 'n' is defined as:
      n! = n * (n-1) * (n-2) * ... * 1

    This function calculates the factorial of 'num':
      num! = num * (num-1) * (num-2) * ... * 1
    
    For example:
      factorial(5) returns 120 because:
      5! = 5 * 4 * 3 * 2 * 1 = 120

    Parameters:
      num (int): The number to compute the factorial of.

    Returns:
      int: The factorial of 'num'.
    """
    # If input is smaller than 0, Error is raised
    if num < 0:
        raise ValueError("num must be a non-negative integer.")
    # Base Case
    if num == 0:
        return 1
    # Recursion Case
    else:
        return num * factorial(num - 1)


def sum_list(arr):
    """
    Recursively computes the sum of a list of numbers.

    This function calculates the sum of a list of numbers:
      arr[0] + arr[1] + arr[2] + ...

    For example:
      sum_list([1, 2, 3, 4, 5, 6]) returns 21 because:
      1 + 2 + 3 + 4 + 5 + 6 = 21

    Parameters:
      arr (list): The list of numbers to sum.

    Returns:
      int: The sum of the numbers in 'arr'.
    """
    # If input is no list, Error is raised
    if not isinstance(arr, list):
        raise ValueError("arr must be a list.")
    # If input array contains anything other than numbers, Error is raised
    if not all(isinstance(item, (int, float)) for item in arr):
        raise ValueError("arr must be a list of numbers.")
    
    # Checking array length
    arr_len = len(arr)
    # Base Case
    if arr_len == 0:
        return 0
    # Recursion Case
    else:
        return arr[0] + sum_list(arr[1:])


def fibonacci(num):
    """
    Recursively computes the sum of the first 'num' Fibonacci numbers.
    
    The Fibonacci sequence is defined as:
      F(0) = 0, F(1) = 0, and F(n) = F(n-1) + F(n-2) for n >= 2.
      
    This function sums the first 'num' Fibonacci numbers:
      F(0) + F(1) + ... + F(num-1)
    
    For example:
      fibonacci(6) returns 12 because:
      0 + 1 + 1 + 2 + 3 + 5 = 12
      
    Parameters:
      num (int): The number of Fibonacci numbers to sum.
    
    Returns:
      int: The sum of the first 'num' Fibonacci numbers.
    """
    # If input is smaller than 0, Error is raised
    if num < 0:
        raise ValueError("num must be a non-negative integer.")
    
    # Recursive Helper Function
    def recur(n, a, b, total):

        # Base Case
        if n == 0:
            return total
        # Recursion Case
        return recur(n - 1, b, a + b, total + a)
    
    return recur(num, 0, 1, 0)


def reverse_string(string):
    """
    Recursively reverses a string.

    This function reverses all elements of a string.

    For example:
      reverse_string("Hello") returns "olleH"

    Parameters:
      string (str): The string to reverse.

    Returns:
      str: The reversed string.
    """
    # If input is no string, Error is raised
    if not isinstance(string, str):
        raise ValueError("input must be a string.")
    
    # Base Case
    if len(string) == 0:
        return ""
    # Recursion Case
    else:
        return string[-1] + reverse_string(string[:-1])


# Testing
def run_tests():
    # Testing factorial()
    print("=== Testing factorial ===")
    # Edge case: factorial of 0
    print("factorial(0) =", factorial(0))  # Expected: 1
    # Small numbers
    print("factorial(1) =", factorial(1))  # Expected: 1
    print("factorial(5) =", factorial(5))  # Expected: 120
    print("factorial(7) =", factorial(7))  # Expected: 5040
    # Negative numbers are not supported (will lead to ValueError)
    for i in range(-3, 0):
        try:
            print(f"factorial({i}) should raise ValueError")
            factorial(i)
        except ValueError as e:
            print("Caught ValueError as expected:", e)
    
    # Testing sum_list()
    print("\n=== Testing sum_list ===")
    # Edge case: empty list
    print("sum_list([]) =", sum_list([]))  # Expected: 0
    # Single element list
    print("sum_list([5]) =", sum_list([5]))  # Expected: 5
    # Multiple elements (positive integers)
    print("sum_list([1, 2, 3, 4, 5, 6]) =", sum_list([1, 2, 3, 4, 5, 6]))  # Expected: 21
    # List with negative numbers
    print("sum_list([-1, -2, -3]) =", sum_list([-1, -2, -3]))  # Expected: -6
    # List with mixed numbers (including floats)
    print("sum_list([1.5, 2.5, 3.0]) =", sum_list([1.5, 2.5, 3.0]))  # Expected: 7.0
    # List that should raise errors
    sum_list_errors = [
        "not a list",
        [1, 2, "three", 4]
    ]
    # Running sum_list_errors in loop
    for arr in sum_list_errors:
        try:
            print(f"sum_list({arr}) should raise ValueError")
            sum_list(arr)
        except ValueError as e:
            print("Caught ValueError as expected:", e)
    
    # Testing fibonacci()
    print("\n=== Testing fibonacci (sum of first 'num' Fibonacci numbers) ===")
    # Edge case: num = 0 (sum of zero Fibonacci numbers)
    print("fibonacci(0) =", fibonacci(0))  # Expected: 0
    # Single number: only F(0)
    print("fibonacci(1) =", fibonacci(1))  # Expected: 0 (only F(0) is summed)
    # Small values
    print("fibonacci(2) =", fibonacci(2))  # Expected: 0 + 1 = 1
    print("fibonacci(3) =", fibonacci(3))  # Expected: 0 + 1 + 1 = 2
    print("fibonacci(6) =", fibonacci(6))  # Expected: 0 + 1 + 1 + 2 + 3 + 5 = 12
    print("fibonacci(7) =", fibonacci(7))  # Expected: 0 + 1 + 1 + 2 + 3 + 5 + 8 = 20
    # Large values
    print("fibonacci(10) =", fibonacci(10)) # Expected: 88
    print("fibonacci(20) =", fibonacci(20)) # Expected: 10945
    print("fibonacci(30) =", fibonacci(30)) # Expected: 1346268
    # Test negative input: should raise a ValueError
    try:
        print("fibonacci(-1) should raise ValueError")
        fibonacci(-1)
    except ValueError as e:
        print("Caught ValueError as expected:", e)
    
    # Testing reverse_string()
    print("\n=== Testing reverse_string ===")
    # Edge case: empty string
    print('reverse_string("") =', '"' + reverse_string("") + '"')  # Expected: ""
    # Single character
    print('reverse_string("a") =', reverse_string("a"))  # Expected: "a"
    # Two characters
    print('reverse_string("ab") =', reverse_string("ab"))  # Expected: "ba"
    # Regular string
    print('reverse_string("Hello") =', reverse_string("Hello"))  # Expected: "olleH"
    # Palindrome (should be the same)
    print('reverse_string("racecar") =', reverse_string("racecar"))  # Expected: "racecar"
    # Numeric string
    print('reverse_string("12345") =', reverse_string("12345"))  # Expected: "54321"
    # Unicode characters
    print('reverse_string("🙂🙃") =', reverse_string("🙂🙃"))  # Expected: "🙃🙂"
    # List that should raise errors
    reverse_string_errors = [
        123,
        [1, 2, 3],
        True,
        None,
        {"key": "value"}
    ]
    # Running reverse_string_errors in loop
    for string in reverse_string_errors:
        try:
            print(f"reverse_string({string}) should raise ValueError")
            reverse_string(string)
        except ValueError as e:
            print("Caught ValueError as expected:", e)

# Main
if __name__ == "__main__":
    run_tests()
