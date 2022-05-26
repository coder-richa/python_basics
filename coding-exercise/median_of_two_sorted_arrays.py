from typing import List
"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

def merge_sorted_lists(nums1: List[int], nums2: List[int]) -> None:
    """ Merge sorted arrays. 
    :param nums1: List[int] first sorted array
    :param nums2: List[int] second sorted array
    """
    # Length of lists.
    size_num1 = len(nums1)
    size_num2 = len(nums2)
    
    # check if both lists are empty.
    if size_num1 == 0 and size_num2 == 0:
        return []
    
    # return nums2 if nums1 is empty.
    if size_num1 == 0:
        return size_num2
    
    # return nums1 if nums2 is empty.
    if size_num2 == 0:
        return size_num1
    
    # List to store merged list.
    merged_list = []
    
    # initial sorted indexes.
    sorted_index_in_num1 = 0
    sorted_index_in_num2 = 0
    
    
    
    # Loop to until one of the list is fully sorted.
    while sorted_index_in_num1 < size_num1 and sorted_index_in_num2 < size_num2:
        
        # Check if nums1 is greater than nums2.
        if nums1[sorted_index_in_num1] <  nums2[sorted_index_in_num2]:
            # Add value from num1 to merge list.
            merged_list.append(nums1[sorted_index_in_num1])
            # Move to next index in nums1.
            sorted_index_in_num1 += 1
        
        # when nums1 is less than nums2.
        else:
            
            # Add value from num2 to merge list.
            merged_list.append(nums2[sorted_index_in_num2])
            
            # Move to next index in nums2.
            sorted_index_in_num2 += 1
    
    # Copy remaining values from nums1 to merge list.
    while sorted_index_in_num1 < size_num1:
        merged_list.append(nums1[sorted_index_in_num1])
        sorted_index_in_num1 += 1
    
    
    # Copy remaining values from nums2 to merge list.
    while sorted_index_in_num2 < size_num2:
        merged_list.append(nums2[sorted_index_in_num2])
        sorted_index_in_num2 += 1

    # Return merged list.
    return merged_list
    

def find_median (nums1: List[int], nums2: List[int]) -> float:
    # Get merged list.
    merged_list = merge_sorted_lists(nums1, nums2)
    
    # Get size of merged list.
    size_merged_list = len(merged_list)
    
    # return 0 if size of merged list is 0.
    if size_merged_list < 1:
        return 0
    
    #  Check if size of merged list is even.
    if size_merged_list % 2 == 0:
        return (merged_list[size_merged_list//2] + merged_list[size_merged_list//2 - 1])/2
    
    # Check if size of merged list is odd.
    else:
        return merged_list[size_merged_list//2]

def main():
    print(find_median(nums1 = [], nums2 = []))
    

if __name__ == '__main__':
    main()
    