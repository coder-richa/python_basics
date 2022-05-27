"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

def convert_to_zigzag(string: str, number_of_rows: int) -> str:
    # Get length of string.
    string_length = len(string)
    
    # when number of rows is 1, return the string as is. 
    if number_of_rows == 1:
        return string

    # Create a list of lists to store the zigzag string.
    zigzag_list=["" for x in range(number_of_rows)]
    
    # Create a variable to keep track of the current row.
    row = 0
     
    # Loop over string charactrers.
    for i in range(string_length):
         
        # Add character to current row.
        zigzag_list[row] += string[i]
 
        # If current row is at the bottom, go to previous row.
        if row == number_of_rows - 1:
            down = False
 
        # If current row is at the top, go to next row.
        elif row == 0:
            down = True
        
        # Update row number
        if down:
            row += 1
        else:
            row -= 1
    # Join the list of lists to get the zigzag string. 
    return ''.join(zigzag_list)
    
    
def main():
    print(convert_to_zigzag("PAYPALISHIRING", 4))

if __name__ == "__main__":
    main()
    
    