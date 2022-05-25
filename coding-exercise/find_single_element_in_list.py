from typing import List
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""


def get_single_value_in_array(arr: List[int]) -> int:
    """
    The function takes an array of numbers and returns the first single value in the array.    
    
    :param arr: list of integers.
    :return: first single value in the array.
    """
    # return -1 if array is empty.
    if len(arr) < 1:
        return -1
    
    # Hold number of times element appeared in array.
    element_occurances = {}
    
    # Loop over all numbers in the range to find the duplicate number.
    for num in arr:
        
        # return the duplicate number
        if num in element_occurances:
            element_occurances[num] += 1
        # Add the number to the dictionary.
        else:
            element_occurances.update({num:1})
    
    # Loop over all numbers in the range to find the single/unique number.
    for element, occurances in element_occurances.items():
        if occurances == 1:
            return element    
        
    # return -1 if no single/unique number found
    return -1

def main():
    print(get_single_value_in_array([1,2,0,0,2,3,3]))

if __name__ == '__main__':
    main()