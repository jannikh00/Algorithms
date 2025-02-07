# Assignment 2: Algorithm Efficiency
# Creating two functions to find the smallest number in an unordered list
# One function has a time complexity of O(n^2) and the other O(n)

# Importing time module for testing purposes
import time

# 1st function - Time Complexity: O(n^2)
def find_minimum_n2(arr):
    # Check if the array is empty
    if not arr:
        # Return None if the array is empty
        return None

    # Initialize count
    count = 0
    # Set min_number to the first element of the list
    min_number = arr[0] 

    # Outer loop to iterate through each number in the list
    # This is my interpretation of the requirement "Iterate through each number and compare it with every other number in the list." in order to find the smallest number in the list
    for i in range(len(arr)):
        # Inner loop to compare the current element with every other element
        for j in range(len(arr)):

            # If current element in inner loop is smaller than current element in outer loop AND smaller than min_number, update min_number
            # I know the check is redundant, but as I said that's how I interpreted the requirement
            if arr[j] < arr[i]:
                if arr[j] < min_number:
                    min_number = arr[j]

            # Increment the count for each iteration
            count += 1

    # Print the count
    print(f"Number of iterations: {count}")

    # Return the smallest number found
    return min_number


# 2nd function - Time Complexity: O(n)
def find_minimum(arr):
    # Check if the array is empty
    if not arr:
        # Return None if the array is empty
        return None

    # Initialize count
    count = 0
    # Set min_number to the first element of the list
    min_number = arr[0]

    # Iterate through the list once
    for num in arr:
        
        # If the current element is smaller than min_number, update min_number
        if num < min_number:
            min_number = num
        
        # Increment the count for each iteration
        count += 1

    # Print the count
    print(f"Number of iterations: {count}")

    # Return the smallest number found
    return min_number


# Testing Functions
def testing(test_arr):
    print("\n")
    # Testing 1st Function
    print(f"Tested List: {test_arr}")
    print("\n")
    print("Testing O(n^2):")
    print("\n")
    start_time = time.time()
    print(f"Result: {find_minimum_n2(test_arr)}")
    end_time = time.time()
    print(f"Exection Time: {end_time - start_time} sec.")

    # Testing 2nd Function
    print("\n")
    print("Testing O(n):")
    print("\n")
    start_time = time.time()
    print(f"Result: {find_minimum(test_arr)}")
    end_time = time.time()
    print(f"Exection Time: {end_time - start_time} sec.")

# Test Cases
testing([4, 8, 1, 7])  # Smallest number: 1
testing([4, 8, 1, 7, 6, 33, 66, 22, 999, 22])  # Smallest number: 1
testing([4, 8, 1, 7, 6, 33, 66, 22, 999, 22, -23, -15, -33, 44])  # Smallest number: -33
testing([100, 200, 300, 400, 500])  # Smallest number: 100
testing([-1, -5, -10, -50, -100])  # Smallest number: -100
testing([99, 0, -99, 1000, -1000])  # Smallest number: -1000
testing([5])  # Smallest number: 5 (Only one element)
testing([7, 7, 7, 7, 7])  # Smallest number: 7 (All elements are the same)
testing([1, -1, 2, -2, 3, -3, 4, -4])  # Smallest number: -4
testing([0, 1, 2, 3, 4, 5, -999])  # Smallest number: -999
testing([3, 2, 1, 0, -1, -2, -3])  # Smallest number: -3