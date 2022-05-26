from typing import List
"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""
def get_first_missing_positive_value_in_array(arr: List[int]) -> int:
    """
    The function takes an array of numbers and returns the minimum positive in the array.    
    :param arr: list of integers
    :return: first missing positive value in the array
    """
    # return -1 if array is empty.
    if len(arr) < 1:
        return -1
    
    # Get unique values of array.
    unique_list = set(arr)
    
    # find max positive number of the array.   
    max_poistive_value = max(unique_list)
    
    # Set current value to 1
    current_positive_value = 1
    
    # Loop over all numbers in the range to find the missing number.
    while current_positive_value <= max_poistive_value:
        # return the missing number
        if current_positive_value not in unique_list:
            return current_positive_value
        
        # Move to next positive number.
        current_positive_value +=1
        
    # return current_positive_value if no missing number found 
    return current_positive_value

def main():
    print(get_first_missing_positive_value_in_array([1,2,0]))

if __name__ == '__main__':
    main()