from typing import List
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""

def get_duplicate_value_in_array(arr: List[int]) -> int:
    """
    The function takes an array of numbers and returns the first duplicate value in the array.    
    
    :param arr: list of integers.
    :return: first duplicate value in the array.
    """
    # return -1 if array is empty.
    if len(arr) < 1:
        return -1
    
    # Get unique values of array.
    unique_elements = set()
    
    # Loop over all numbers in the range to find the duplicate number.
    for num in arr:
        
        # return the duplicate number
        if num in unique_elements:
            return num
        # Add the number to the set.
        else:
            unique_elements.add(num)
        
        
    # return -1 if no duplicate number found
    return -1

def main():
    print(get_duplicate_value_in_array([1,2,0,2,3]))

if __name__ == '__main__':
    main()