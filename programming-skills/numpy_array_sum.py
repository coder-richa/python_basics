""" 
Task

You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24
Explanation

The sum along axis  = [ ]
The product of this sum = 
"""

import numpy
from typing import List

def read_values() ->List:
    values = input().strip()
    value_list = values.split()
    return list(map(lambda a: int(a),value_list))

if __name__ == "__main__":
    n,m = read_values()
    ls = []
    
    for row in range(n):
        ls.append(read_values())  
    
    my_array = numpy.array(ls)
    addition = numpy.sum(my_array, axis = 0)
    # print(addition)
    print(numpy.prod(addition))        


