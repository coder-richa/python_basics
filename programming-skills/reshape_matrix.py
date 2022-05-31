from ast import Break
from typing import List

""" 
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""

def reshape_matrix(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    
    # Check if the reshape operation is possible.
    prev_rows_number = len(mat)
    if prev_rows_number < 0:
        return mat

    prev_columns_number = len(mat[0])    
    # check if there are sufficient elements to rearrange.
    if prev_rows_number * prev_columns_number != r * c:
        return mat
    
    # Variables to track the current position.
    sorted_row =0
    sorted_column =0
    
    # Create list with rows and columns.
    result = [[0]*c for _ in range(r)]
    
    # Populate transformation array.
    for i in range(r):
        
        for j in range(c):
            result[i][j]=mat[sorted_row][sorted_column]
            # Move to next element.
            sorted_column+=1
            
            # Move to next row for data.
            if sorted_column >= prev_columns_number:
                sorted_column = 0
                sorted_row += 1
    
    # Return transformation.
    return result

def main():
    print(reshape_matrix(mat = [[1,2],[3,4]], r = 1, c = 4))
    
if __name__ == "__main__":
    main()
