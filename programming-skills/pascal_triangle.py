from typing import List
""" 
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""

def pascal_triangle(numRows: int) -> List[List[int]]:
    # Insuffient number of rows.
    if numRows < 1:
        return []

    pascal_triangle_list = [ [1] for i in range(numRows)]
    
    for range_index in range(1,numRows):
        for index in range(1,range_index+1):
            if len(pascal_triangle_list[range_index-1]) > index:
                
                pascal_triangle_list[range_index].append(pascal_triangle_list[range_index-1][index-1] + pascal_triangle_list[range_index-1][index])
            else:
                pascal_triangle_list[range_index].append(1)
    return pascal_triangle_list


def main():
    print(pascal_triangle(numRows = 5))
    
if __name__ == "__main__":
    main()
    