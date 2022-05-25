from typing import List
"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""

def get_missing_value_in_array(arr: List[int]) -> int:
    """
    The function takes an array of numbers and returns the missing number in the array.    
    :param arr: list of integers
    :return: missing value in the array
    """
    # range of the array
    n = len(arr)    
    lower_limit = 0
    upper_limit = n + 1
    
    # set of unique numbers in the array
    arr = set(arr)
    
    # Loop over all numbers in the range to find the missing number
    for i in range(lower_limit, upper_limit):
        if i not in arr:
            # return the missing number
            return i
    # return -1 if no missing number found 
    return -1


def main():
    arr =  [0,1]
    print(get_missing_value_in_array(arr))
        

if __name__ == '__main__':
    main()
    