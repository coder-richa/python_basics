from typing import List
""" 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def contains_duplicate( nums: List[int]) -> bool:
    # Get total elements in list.
    total_elements = len(nums)
    
    # Check if number of elements is within range.
    if total_elements < 1 or total_elements > 10**6:
        return False
    
    # Get unique elements in list.
    total_unique_elements = len(set(nums))
    
    # Compare the total unique elements with total elements.
    return total_elements != total_unique_elements


def main():
    print(contains_duplicate([1,2,0,2,3]))

if __name__ == '__main__':
    main()