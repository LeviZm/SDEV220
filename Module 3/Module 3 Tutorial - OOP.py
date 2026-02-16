'''
Module 3 Tutorial - Functional Programming vs OOP
Levi Melangton

Object Oriented Programming (OOP) portion of the Module 3 Tutorial Assignment.
This program sorts an Array of 0s, 1s, and 2s in ascending order--without using built-in sorting functions.

Constraits:
1 <= arr.size() <= 10^6
0 <= arr[i] <= 2

Variables in main:
test_cases: List containing the unsorted arrays of integers to be sorted.
sol: Instance of the Solution class to call the sort012 method and print the results.

Variables in sort012 method:
low = 0: Pointer to track the position of the next 0.
mid = 0: Pointer to track the current element being processed.
high = len(arr) - 1: Pointer to track the position of the next 2
'''
class Solution:
    def sort012(self, arr):
        # Initialize pointers for the current position of 0s, 1s, and 2s
        low = 0
        mid = 0
        high = len(arr) - 1

        # Move through the array and sort the elements
        while mid <= high:
            if arr[mid] == 0: # Check if current element is 0
                arr[low], arr[mid] = arr[mid], arr[low] # Swap the elements at low and mid
                low += 1 # move the lower pointer to the next index to the "right"
                mid += 1 # move the middle pointer to the next index to the "right"
            elif arr[mid] == 1: # Check if current element is 1
                mid += 1 # move the middle pointer to the next index
            else: # only option left is 2
                arr[mid], arr[high] = arr[high], arr[mid] # Swap the elements at middle pointer and high pointer
                high -= 1 # move the high pointer to the next index to the "left"
    
        return arr

def main():
    test_cases = [
        [0, 1, 2, 0, 1, 2],
        [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    ]

    for i, arr in enumerate(test_cases, 1):
        original = list(arr) # Store the original array for printing
        print(f"Test Case {i}:")
        print(f"Original array: {original}")

        # Create an instance of the Solution class to call the sort012 method
        sol = Solution()
        sorted_arr = sol.sort012(arr)
        print(f"Sorted array: {sorted_arr}\n")

if __name__ == "__main__":
    main()