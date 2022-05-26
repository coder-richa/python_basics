from typing import List
""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

def two_sum( nums: List[int], target: int) -> List[int]:
    # Hold total number of elements in the list.
    total_numbers = len(nums)
    # Dictionary to hold the element as key and its index as corresponding value.
    checked_elements = {}
    
    # Loop over all elements in array.
    for i in range(0, total_numbers):
        
        current_number = nums[i]
        second_number = target - current_number
        
        # return index of second and first number if it is in the dictionary.
        if second_number in checked_elements:
            return [i, checked_elements[second_number]]
        
        # append current number to dictionary.
        checked_elements[current_number] = i
        
    # No element found. 
    return []


def main():
        print(two_sum(nums = [2,7,11,15], target = 9))

if __name__ == '__main__':
    main()   