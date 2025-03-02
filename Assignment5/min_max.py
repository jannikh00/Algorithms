# Assignment 5: Min and Max Divide and Conquer

# This python file contains two algorithms that take an unordered list and use the divide and conquer approach to find the 
# 1) minimum value and 2) maximum value recursively.

def find_max(lst):
    """
    Recursively finds the maximum value in a list of numbers.

    This function finds the maximum value in a list of numbers recursively by comparing the first element of the list
    with the maximum value of the rest of the list. The function calls itself with a smaller sublist until it finds
    the maximum value.

    For example:
        find_max([34, 7, 23, 32, 5, 62]) returns 62.0

    Parameters:
        lst (list): The list of numbers to find the maximum value of.

    Returns:
        float: The maximum value in the list.
        
    Raises:
        ValueError: If the list is empty.
        ValueError: If the list contains anything other than numbers.
    """
    # If List is empty, throw Error
    if not lst:
        raise ValueError("List is empty.")
    
    # If List contains anything other than numbers, throw Error
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numbers.")


    # Base Case
    if len(lst) == 1:
        return float(lst[0])

    def findMaximumElement(i, j, lst):
        """
        Recursively finds the maximum value in a sublist of numbers.

        This helper function uses the divide-and-conquer approach to find the maximum element
        by dividing the list into sublists and recursively finding the maximum of each sublist.
        It then compares the results from the sublists to find the overall maximum.

        Parameters:
            i (int): The starting index of the sublist.
            j (int): The ending index of the sublist.
            lst (list): The list of numbers to find the maximum value from.

        Returns:
            float/int: The maximum value in the sublist.
        """        
        # Base Case
        if i == j:
            return lst[i]
        # Finding the middle of current list
        mid = (i + j) // 2
        # Recursion Case
        return max(findMaximumElement(i, mid, lst), findMaximumElement(mid + 1, j, lst))
    
    # Recursion Case
    return float(findMaximumElement(0, len(lst) - 1, lst))

def find_min(lst):
    """
    Recursively finds the minimum value in a list of numbers.

    This function findsinimum value in a list of numbers recursively by comparing the first element of the list
    with the minimum value of the rest of the list. The function calls itself with a smaller sublist until it finds
    the minimum value.

    For example:
        find_min([34, 7, 23, 32, 5, 62]) returns 5.0

    Parameters:
        lst (list): The list of numbers to find the minimum value of.

    Returns:
        float: The minimum value in the list.

    Raises:
        ValueError: If the list is empty.
        ValueError: If the list contains anything other than numbers.
    """
    # If List is empty, throw Error
    if not lst:
        raise ValueError("List is empty.")
    
    # If List contains anything other than numbers, throw Error
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("List must contain only numbers.")

    # Base Case
    if len(lst) == 1:
        return float(lst[0])
    
    def findMinimumElement(i, j, lst):
        """
        Recursively finds the minimum value in a sublist of numbers.

        This helper function uses the divide-and-conquer approach to findinimum element
        by dividing the list into sublists and recursively finding the minimum of each sublist.
        It then compares the results from the sublists to find the overall minimum.

        Parameters:
            i (int): The starting index of the sublist.
            j (int): The ending index of the sublist.
            lst (list): The list of numbers to find the minimum value from.

        Returns:
            float/int: The minimum value in the sublist.
        """        
        # Base Case
        if i == j:
            return lst[i]
        # Finding the middle of the current list
        mid = (i + j) // 2
        # Recursion Case
        return min(findMinimumElement(i, mid, lst), findMinimumElement(mid + 1, j, lst))
    
    # Recursion Case
    return float(findMinimumElement(0, len(lst) - 1, lst))



# Testing
def run_tests():
    # Testing find_max
    print("\n=== Testing find_max ===")
        # Test cases for find_max in a dictionary - Tupel (later converted to list): Float
    test_cases = {
        (34, 7, 23, 32, 5, 62): 62.0,
        (15, 3, 20, 1): 20.0,
        (99, 72, 18, 44, 60, 11, 85, 23, 30) : 99.0,
        (22,): 22.0, # List with one element
        (): "ValueError", # Empty list
        (1, 2, "three", 4): "ValueError", # List with string
        (3.5, 7.1, 2.3, 9.8, 5.6): 9.8, # Floats
        (-34, -7, -23, -32, -5, -62): -5.0, # Negative Numbers
        (5, 5, 5, 5, 5): 5.0, # All Elements identical
        (-10, -20, 30, 40, -50): 40.0, # Negative and Positive Elements
        (3, 1.5, 7, 2.5): 7.0, # List with Integers and Floats
        (1e6, 1e-6, 3, -1e6, 1.1): 1000000.0, # Very large and very small numbers
        (1, 2, None, 4): "ValueError" # List with None
    }

    # Loop iterating through test cases catching possible errors, tupels being converted to lists first 
    for numbers, expected in test_cases.items():
        try:
            print(f"\nTested List: {list(numbers)}")
            print(f"Expected Result: {expected}")
            print(f"Actual Result: {find_max(list(numbers))}")
        except ValueError as e:
            print("Caught ValueError as expected:", e)

    # Testing find_min
    print("\n=== Testing find_min ===")
    # Test cases for find_min in a dictionary - Tupel (later converted to list): Float
    test_cases ={
        (34, 7, 23, 32, 5, 62): 5.0,
        (15, 3, 20, 1): 1.0,
        (99, 72, 18, 44, 60, 11, 85, 23, 30) : 11.0,
        (22,): 22.0, # List with one element
        (): "ValueError", # Empty list
        (1, 2, "three", 4): "ValueError", # List with string
        (3.5, 7.1, 2.3, 9.8, 5.6): 2.3, # Floats
        (-34, -7, -23, -32, -5, -62): -62.0, # Negative Numbers
        (5, 5, 5, 5, 5): 5.0, # All Elements identical
        (-10, -20, 30, 40, -50): -50.0, # Negative and Positive Elements
        (3, 1.5, 7, 2.5): 1.5, # List with Integers and Floats
        (1e6, 1e-6, 3, -1e6, 1.1): -1000000.0, # Very large and very small numbers
        (1, 2, None, 4): "ValueError" # List with None
    }

    # Loop iterating through test cases catching possible errors, tupels being converted to lists first
    for numbers, expected in test_cases.items():
        try:
            print(f"\nTested List: {list(numbers)}")
            print(f"Expected Result: {expected}")
            print(f"Actual Result: {find_min(list(numbers))}")
        except ValueError as e:
            print("Caught ValueError as expected:", e)


# Main
if __name__ == "__main__":
    run_tests()