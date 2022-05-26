from typing import List
from math import inf
""" 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""

def maximum_subarray(nums: List[int]) -> int:
    # Get total number of elements in list.
    total_number_of_elements = len(nums)
    # Check if list is empty.
    if total_number_of_elements < 1:
        return 0
    

    # Initialize variable to hold maximum sum of subarray.
    max_total_of_subarray = nums[0]
    new_total_of_subarray = 0
    # start and end index specyfies the subarray.
    # start_index = 0
    # end_index = 0
    
    # Loop over all elements to calculate maximum sum.
    for index in range(0,total_number_of_elements):
        # add current element to new_total_of_subarray.
        new_total_of_subarray += nums[index] 
        
        # Update max total of subarray.
        if max_total_of_subarray < new_total_of_subarray:
            max_total_of_subarray = new_total_of_subarray
            # Track the end index of subarray.
            # end_index = index
            
        # reset start index and new total of subarray. 
        if new_total_of_subarray < 0:
            
            # start_index = index + 1
            new_total_of_subarray = 0
            
    # Return max total of subarray.
    return max_total_of_subarray
  
def main():
        print(maximum_subarray([5,4,-1,7,8]))

if __name__ == '__main__':
    main()   