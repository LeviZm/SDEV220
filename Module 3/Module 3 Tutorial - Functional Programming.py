'''
Module 3 Tutorial - Functional Programming vs OOP
Levi Melangton

Module 3 Tutorial - Functional Programming portion of the Module 3 Tutorial Assignment.
This program takes a sorted array arr[] and an integer k, and it returns the index position of k in arr[] using binary search.
If k doesn't exist in arr[], the function returns -1.
Note: If multiple occurrences of k exist in arr[], the function should return the index position of the smallest index.

Constraints:
1 <= arr.size() <= 10^5
1 <= arr[i] <= 10^6
1 <= k <= 10^6

Variables in main:
test_cases: List containing the sorted arrays of integers and the corresponding k values to search for.

Variables in binary_search function:
left = 0: Pointer to track the leftmost index of the search range.
right = len(arr) - 1: Pointer to track the rightmost index of the search range.
'''

# Function to perfrom the binary search algorithm
class Solution:
    def __init__(self, arr, k, test_number):
        self.arr = arr # Initialize arr to store the array being searched
        self.k = k # Initialize k to store the value being searched for
        self.result = -1 # Initialize result to -1 to indicate that k has not been found yet

    def binary_search(self):
        left = 0 # Initialize left pointer to the first index of the array
        right = len(self.arr) - 1 # Initialize right pointer to the last index of the array

        # Loop through the array until the value is found or the search range is exhausted
        while left <= right:
            mid = left + (right - left) // 2 # Initialize and calculate the middle index of the current search range

            if self.arr[mid] == self.k: # Check if the middle element is the value we are looking for
                self.result = mid # If it is, update result to the current middle index if k is found
                right = mid - 1  # Continue searching in the left half in case the value is found at a smaller index
            elif self.arr[mid] < self.k: # Check if the middle element is less than k
                left = mid + 1 # If it is, move the left point to the right of the middle index to continue searching in the right half
            else: # Check if the middle element is greater than k
                right = mid - 1 # If it is, move the right point to the left of the middle index to continue searching in the left half

        return self.result # Return the result if found, if not it was initialzed to -1
    
    def print_results(self, test_number): # Pass test_number as an arguement to identify which test case is being printed
        print(f"arr{test_number}[] = {self.arr}, k = {self.k}, result: {self.result}\n")

def main():
    # Initialize a list of the input arrays and the corresponding values to search for
    test_cases = [
        ([11,22,33,44,55], 44), # Test case 1
        ([1,2,3,4,5], 6), # Test case 2
        ([1,1,1,1,2], 1) # Test case 3
    ]

    # Loop through the test cases to create solution instances
    for i, (arr,k) in enumerate(test_cases, 1):
        sol = Solution(arr, k, i) # Create an instance of the Solution class for the current test case
        sol.result = sol.binary_search() # Call the binary_search method and store the result in the instance variable
        sol.print_results(i) # Print the results for the current test case using the print_results method

if __name__ == "__main__":
    main()
