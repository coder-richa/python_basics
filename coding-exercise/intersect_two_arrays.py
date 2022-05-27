from typing import List
""" 
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 
"""

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # Get length of both lists.
    length_of_list_1 = len(nums1)
    length_of_list_2 = len(nums2)
    
    # Check if length of lists are with in range.
    if not (1 <= length_of_list_1 <= 1000 and 1 <= length_of_list_2 <= 1000):
        return []
    
    # Get Unique elements from both lists.
    common_unique_elements_in_both_lists = set(nums1).intersection(set(nums2)) 
    
    # List to hold common elements from both lists.
    common_elements = []
    
    # Loop to find the common elements from both lists.
    for element in common_unique_elements_in_both_lists:
        # Find the count of common elements in both lists.
        number_of_occurances_in_both_lists = min(nums1.count(element), nums2.count(element))
        # Append to list.
        common_elements.extend([element] * number_of_occurances_in_both_lists)
    
    # Return the list of common elements.
    return common_elements
    

def main():
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(intersect(nums1, nums2))
    
if __name__ == "__main__":
    main()
    