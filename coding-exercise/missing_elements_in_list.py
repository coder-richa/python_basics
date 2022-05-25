from typing import Dict, List ,Tuple
"""
Write a function in the language of your choice that accepts an
 arbitrary number of lists of natural numbers, each list of arbitrary length,
 and returns all the gaps that exist in the union of all the lists.
 For example the lists { 3, 5 } { 2, 7, 3 } { 6 } = { 2, 3, 5, 6, 7 }
 have a gap of length 1 starting at the number 3.  
"""


def calculate_gap(numbers: List[int]) -> Dict:
    """
    Calculate the gap between two consecutive numbers in a list, 
    and save the gap starting point and length of the gap in a dictionary.
    
    :param numbers: List of numbers.
    :return: Dictionary with gap starting point and length of the gap.
    """
    gap = {}
    
    # Loop over all elements to find the gap
    for i in range(len(numbers) - 1):
        # When gap greater than 1, save the gap starting point and length of the gap
        if numbers[i + 1] - numbers[i]  > 1:
            length_of_gap = numbers[i + 1] - numbers[i] -1
            gap[numbers[i]] = length_of_gap        
    return gap


def sort_list_union(*numbers: Tuple[List[int]]) -> List[int]:
    """
    Union of multiple lists in sorted order.
    
    :param numbers: List of numbers.
    :return: Union of the  lists in sorted order. 
    """
    union_list = []
    
    # Concatenate all lists
    for list_data in numbers:
        union_list += list_data
    
    # Sort the list and return the union 
    return sorted(set(union_list))


def calculate_gap_union(*numbers: Tuple[List[int]]) -> Dict:
    """
    Calculate the gap between two consecutive numbers in a list, 
    and save the gap starting point and length of the gap in a dictionary.
    
    :param numbers: List of numbers.
    :return: Dictionary with gap starting point and length of the gap.
    """
    # Get sorted union of all lists
    union_list = sort_list_union(*numbers)
    
    # Get Gap dictionary
    gap = calculate_gap(union_list)
    
    # return the gap dictionary
    return gap


def main():
    numbers = [2,3],[3,5,7],[6,10,15]
    gap = calculate_gap_union(*numbers)
    for gap_starting_point, gap_length in gap.items():
        print(f"There is a gap of {gap_length} starting at {gap_starting_point}")

if __name__ == "__main__":
    main()    