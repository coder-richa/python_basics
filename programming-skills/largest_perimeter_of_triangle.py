from typing import List
""" 
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area,
return 0.
Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
"""

def largest_perimeter(  nums: List[int]) -> int:
    # Count number of elements in array.
    numbers_count = len(nums)
    #  Check if there are at least 3 elements in array.
    if numbers_count < 3:
        return 0
    
    # Variable to hold the largest perimeter.
    largest_perimeter = 0
    
    # Sort numbers in ascending order.
    nums.sort(reverse=True)
    
    # Loop to check numbers with largest perimeter.
    for i in range(numbers_count - 2):
        
        # Check if triangle can be formed.
        if nums[i] < nums[i+1] + nums[i+2]:            
            largest_perimeter = max(largest_perimeter,nums[i] + nums[i+1] + nums[i+2])
            break
    
    # Return largest perimeter.
    return largest_perimeter

def main():
    print(largest_perimeter(nums = [5,4,2]) )

if __name__ == "__main__":
    main()
    